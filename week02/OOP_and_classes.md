
A class is a blueprint. It describes what data each thing of that kind will hold and which functions (methods) can act on that data, but it holds no contacts itself. ContactBook is a class: it says "a contact book has a file path and a dict of contacts, and it can add, look up, delete, and count."

An object, or instance, is one concrete thing built from that blueprint. book = ContactBook(Path("contacts.json")) creates an object. If I wrote work = ContactBook(Path("work.json")) as well, I'd have two separate objects from the same class, each with its own _path and its own _contacts dict. Adding someone to work does nothing to book. The class is written once; objects can be made as many times as needed.

The split is this: methods live on the class and are shared, while data lives on each object and is separate. There is only one add function in memory, but every ContactBook object has its own contacts.

Because there's only one add function shared by every object, it needs to be told which object's data to change. That's what self does. When I write book.add("Ana", "555"), Python quietly turns it into ContactBook.add(book, "Ana", "555"). The object before the dot gets passed in as the first argument, and by convention that parameter is named self. Inside the method, self._contacts means "this particular object's contacts."

That's why every normal method has self as its first parameter. Python always passes the object in, so the method has to have a slot to receive it. self is a naming convention, not a keyword, but nobody uses a different name.

Two bugs follow from this. If I forget self in the def line, calling the method gives TypeError: add() takes 2 positional arguments but 3 were given, because Python passed the object in and there was no parameter for it. If I forget the self. prefix inside a method (writing _contacts = {} instead of self._contacts = {}), I create a local variable that disappears when the method returns, and the object never gets the data. The general pattern is that anything meant to outlast a single method call has to be attached to self.

__init__ runs automatically right after a new object is created. At that point self is a fresh, empty object, and __init__'s job is to attach its starting data: self._path = path and self._contacts = self._load().

The leading underscore on _contacts, _load, and _save is also a convention. It means "internal: code outside the class shouldn't touch this." Python doesn't enforce it, but it marks which parts are the public interface (add, lookup, delete, count) and which are internal details.

Did the contact book get easier or harder to reason about?

In some ways it got easier. In the dict version, the contacts and the file they're saved to were separate things, and whoever changed the dict had to remember to save afterwards. In the class, add and delete call _save themselves, so it's impossible to change a contact and forget to write it to disk. The rule "the file matches what's in memory" is now enforced in one place instead of being a habit the calling code has to keep up. The main block can't change the dict directly either. It can only use named operations, and each one returns something with a clear meaning (str | None for the old number, bool for whether the delete happened). The menu loop now reads as "ask the book, print what it says," which is easier to follow than code that mixes dict manipulation with printing.

In other ways it got harder. There's more indirection: to know what book.add does, I have to jump to the class, whereas before the dict operation was right there in the loop. The state is hidden, so I can't just print(contacts) to see everything without adding a method for it. There's also a side effect that isn't visible where it happens: book.add(...) writes to disk, and nothing on that line says so. And self. appears everywhere, which is noise the dict version didn't have.

Honest verdict: for a program with four operations, the class is only somewhat better. The real gain is tying the data to the file and forcing logic to stay separate from display, not any reduction in size. A class earns its keep when there's a rule to protect, like "always saved" here or "can't withdraw more than the balance" in the bank account example. A class that is just a dict with methods and no rules is mostly extra ceremony. One practical bonus shows up later: because the path is passed into __init__, tests can create ContactBook(tmp_path / "contacts.json") and never touch the real file.

what's the difference between a dict-based record and a class-based object representing the same data — same "Player," described two ways?

As a dict:
player = {"id": 7, "name": "George", "score": 120}

As a class:
class Player:
    def __init__(self, id: int, name: str, score: int = 0) -> None:
        self.id = id
        self.name = name
        self.score = score

    def add_points(self, points: int) -> None:
        if points < 0:
            raise ValueError("points must be non-negative")
        self.score += points

player = Player(7, "George", 120)

Both hold the same three values. The difference is what's guaranteed and who is in charge of the rules.

A dict is a bag of key-value pairs with no fixed shape. Nothing forces a Player dict to have a "name" key, so one part of the program can build {"id": 7, "nmae": "George"} and nothing complains until some distant line does player["name"] and crashes with a KeyError, far from where the mistake happened. The typo also creates an extra key without any error. Any code anywhere can do player["score"] = -500 or player["score"] = "lots", because a dict has no opinion about its contents. And a dict has no behavior: the rule "points added can't be negative" has to live in some function elsewhere, and every piece of code that touches score has to remember to go through that function. Nothing stops it from skipping it.

What the dict does have going for it is that it's exactly the shape data takes at the edges of a program. json.load gives you dicts, a database row maps naturally onto one, and an HTTP request body arrives as one. Dicts are cheap, transparent, and easy to print and serialize.

The class declares the shape once, in __init__. You can't create a Player without an id and a name, because the constructor requires them. That turns a missing field from a crash somewhere later into an error on the exact line where the Player is created. Your editor and type checker also know that a Player has .score, so a typo like player.scroe gets flagged before the code even runs.

To be honest about the limits: plain Python still lets you do player.score = -500 from outside, or assign a misspelled attribute without error. A class doesn't make this impossible. It gives the rules one obvious home (add_points) and makes going around them a visible violation rather than the normal way of working. A @dataclass removes the __init__ boilerplate, and frozen=True or properties can tighten things further, but the core idea stays the same.

The deeper difference is that the class holds both data and behavior. The rule about points lives next to the data it protects, so anyone reading Player sees the whole contract in one place.

There's also a subtle difference in equality. Two dicts with the same contents compare equal with ==. Two plain class instances with the same values are not equal by default, because Python compares objects by identity unless you define __eq__ (a dataclass defines it for you). This matters in Week 6: an entity like a Player is defined by its id, not by its current score, so you'll have to decide deliberately what "same player" means.

