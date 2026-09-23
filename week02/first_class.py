
class Contact:
    def __init__(self, name: str, phone: str) -> None:
        self.name = name
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

if __name__ == "__main__":
    ana = Contact("Ana", "555-1234")
    bob = Contact("Bob", "555-9876")
    cara = Contact("Cara", "555-4567")

    print(ana)
    print(bob)
    print(cara)