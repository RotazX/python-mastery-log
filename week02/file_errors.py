
def file_reader(path: str) -> tuple[list[str] | None, str | None]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines(), None
    except FileNotFoundError:
        return None, f"There is no such file as {path}."

def main() -> None:
    file = input("Write a file name! ")
    value, error = file_reader(file)
    if error is None:
        for line in value:
            print(line, end="")
    else:
        print(error)

if __name__ == "__main__":
    main()
                                   