
def join_messages(*messages: str) -> str:
    return " | ".join(messages)

def build_profile(name: str, **fields: str) -> dict[str, str]:
    fields["name"] = name
    return fields

if __name__ == "__main__":
    print(join_messages("start", "load", "done"))
    print(join_messages())
    print(join_messages(*["a", "b"]))

    print(build_profile("Anna", city="Tallinn", role="dev"))
    print(build_profile("Bob"))