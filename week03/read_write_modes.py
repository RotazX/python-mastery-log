from pathlib import Path

# def write_text(path: Path, text: str) -> None:
#     path.write_text(text)

def write_text(path: Path, text: str) -> None:
    with open(path, mode="w") as f:
        f.write(text + "é")

def read_text(path: Path) -> str:
    with open(path, mode="r") as f:
        return f.read()

def append_text(path: Path, text: str) -> None:
    with open(path, mode="a") as f:
        f.write(text)

def read_bytes(path: Path) -> bytes:
    with open(path, mode="rb") as f:
        return f.read()

def write_bytes(path: Path, data: bytes) -> None:
    with open(path, mode="wb") as f:
        f.write(data)


if __name__ == "__main__":
    base = Path(__file__).parent / "sandbox" / "a.txt"
    base2 = Path(__file__).parent / "sandbox" / "b.txt"

    try:
        write_bytes(base, "hello") 
    except TypeError as e:
        print(f"Crashed as predicted!")
        print(f"Error type: {type(e).__name__}")
        print(f"Last line message: {e}\n")

    write_bytes(base, b"hello")

    write_text(base, "hello")
    write_text(base2, "second")

    append_text(base, "world")

    result = read_text(base)
    print(repr(result))
    print(type(result))

    bytes_result = read_bytes(base)
    print(repr(bytes_result))
    print(type(bytes_result))