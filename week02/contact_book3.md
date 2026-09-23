import json
from pathlib import Path


class ContactBook:
    def __init__(self, path: Path) -> None:
        self._path = path
        self._contacts: dict[str, str] = self._load()

    def _load(self) -> dict[str, str]:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save(self) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(self._contacts, f, indent=2)

    def add(self, name: str, phone: str) -> str | None:
        old_phone = self._contacts.get(name)
        self._contacts[name] = phone
        self._save()
        return old_phone

    def lookup(self, name: str) -> str | None:
        return self._contacts.get(name)

    def delete(self, name: str) -> bool:
        if name not in self._contacts:
            return False
        del self._contacts[name]
        self._save()
        return True

    def count(self) -> int:
        return len(self._contacts)


if __name__ == "__main__":
    book = ContactBook(Path("contacts.json"))
    print(f"Loaded {book.count()} contact(s).")

    while True:
        print("\n1. Add 2. Look up 3. Delete 4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            old_phone = book.add(name, phone)
            if old_phone is not None:
                print(f"Overwrote existing number for {name} ({old_phone}).")
            print(f"Saved {name}: {phone}")
        elif choice == "2":
            name = input("Name: ")
            phone = book.lookup(name)
            if phone is None:
                print(f"No contact named {name}.")
            else:
                print(f"{name}: {phone}")
        elif choice == "3":
            name = input("Name: ")
            if book.delete(name):
                print(f"Deleted {name}.")
            else:
                print(f"No contact named {name}.")
        elif choice == "4":
            break
        else:
            print("Not a valid choice.")