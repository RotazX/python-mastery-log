
def get_int(raw: str | int) -> tuple[int | str, str]:
    try:
        value = int(raw)
    except ValueError:
        return None, f"{raw!r} is not a whole number" # return raw, "is not a number" - this is wrong
    else:
        return raw, None # return raw, "is a number!" - this is wrong

def main() -> None:
    value, error = get_int(input("Write me a number. "))
    if error is None:
        print(f"{value} is a number!")
    else:
        print(error)

if __name__ == "__main__":
    main()
    