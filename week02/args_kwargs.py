
"""
args_kwargs.py — a beginner's tour of *args and **kwargs

Normally a function has a FIXED number of inputs:

    def add(a, b):
        return a + b

    add(1, 2)       # works
    add(1, 2, 3)    # ERROR: too many arguments

*args and **kwargs let a function accept ANY number of inputs.

    *args    -> collects extra POSITIONAL arguments into a TUPLE
                (arguments passed by position: log("a", "b", "c"))

    **kwargs -> collects extra KEYWORD arguments into a DICTIONARY
                (arguments passed by name: build_profile(name="George"))

The names "args" and "kwargs" are just conventions. The stars (* and **)
are what do the actual work.
"""


# ---------------------------------------------------------------------------
# PART 1: *args
# ---------------------------------------------------------------------------

def log(*messages):
    """Print any number of messages as one log line."""
    # Inside the function, `messages` is a tuple, e.g. ("Server", "started")
    print(f"  (messages is a {type(messages).__name__}: {messages})")

    line = " | ".join(str(m) for m in messages)
    print(f"[LOG] {line}")


def add_all(*numbers):
    """Add up however many numbers you give it."""
    total = 0
    for n in numbers:
        total += n
    return total


# ---------------------------------------------------------------------------
# PART 2: **kwargs
# ---------------------------------------------------------------------------

def build_profile(**fields):
    """Build a user profile from any named fields you pass in."""
    # Inside the function, `fields` is a dict, e.g. {"name": "George", "age": 19}
    print(f"  (fields is a {type(fields).__name__}: {fields})")

    profile = {}
    for key, value in fields.items():
        profile[key] = value
    return profile


# ---------------------------------------------------------------------------
# PART 3: mixing normal arguments with *args and **kwargs
# ---------------------------------------------------------------------------

def order_pizza(size, *toppings, **extras):
    """
    size      -> a normal, required argument
    *toppings -> any number of toppings
    **extras  -> any optional named settings
    Order matters: normal args first, then *args, then **kwargs.
    """
    print(f"A {size} pizza")
    if toppings:
        print(f"  Toppings: {', '.join(toppings)}")
    for key, value in extras.items():
        print(f"  {key}: {value}")


# ---------------------------------------------------------------------------
# Run the examples
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== *args: log() ===")
    # Same function, different number of arguments each time:
    log("Server started")
    log("User logged in", "id=42")
    log("Error", "disk full", "code=507", 3.14)
    # Why useful: you don't have to decide in advance how many pieces
    # a log message will have. print() itself works exactly this way!

    print("\n=== *args: add_all() ===")
    print(add_all(1, 2))            # 3
    print(add_all(1, 2, 3, 4, 5))   # 15
    print(add_all())                # 0  (no arguments is fine too)

    print("\n=== **kwargs: build_profile() ===")
    george = build_profile(name="George", city="Tallinn", learning="Python")
    print(george)

    minimal = build_profile(name="Anna")
    print(minimal)
    # Why useful: every profile can have different fields, and you
    # never have to change the function to support a new one.

    print("\n=== Mixing them: order_pizza() ===")
    order_pizza("large", "mushrooms", "olives", "cheese",
                delivery=True, extra_sauce="garlic")
    order_pizza("small")  # only the required argument

    print("\n=== Bonus: stars work in reverse too (unpacking) ===")
    words = ["unpacked", "from", "a", "list"]
    log(*words)          # same as log("unpacked", "from", "a", "list")

    settings = {"name": "Bot", "version": 2}
    print(build_profile(**settings))  # same as build_profile(name="Bot", version=2)