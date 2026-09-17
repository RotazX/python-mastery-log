"""Practice with try / except / else / finally.

Every function here returns a (result, error) tuple: exactly one of the two
is None. Nothing in this file prints except main().
"""


def parse_int(raw: str) -> tuple[int | None, str | None]:
    try:
        value = int(raw)
    except ValueError:
        return None, f"{raw!r} is not a whole number"
    else:
        return value, None


def divide(numerator: float, denominator: float) -> tuple[float | None, str | None]:
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return None, "cannot divide by zero"
    else:
        return result, None


def read_file(path: str) -> tuple[str | None, str | None]:
    try:
        handle = open(path, encoding="utf-8")
    except FileNotFoundError:
        return None, f"no file at {path!r}"
    else:
        with handle:
            return handle.read(), None


def read_file_manual(path: str) -> tuple[str | None, str | None]:
    """Same job as read_file, but closing the handle by hand.

    This is what `with` does for you. Written out once so you can see why
    `finally` exists: the close has to happen whether the read succeeds,
    raises, or returns early.
    """
    handle = None
    try:
        handle = open(path, encoding="utf-8")
        contents = handle.read()
    except FileNotFoundError:
        return None, f"no file at {path!r}"
    else:
        return contents, None
    finally:
        if handle is not None:
            handle.close()


def trace_clause_order(raw: str) -> list[str]:
    """Return the clauses that ran, in order, for a given input."""
    trace: list[str] = ["try entered"]
    try:
        int(raw)
    except ValueError:
        trace.append("except ran")
    else:
        trace.append("else ran")
    finally:
        trace.append("finally ran")
    return trace


def main() -> None:
    for raw in ("42", "abc"):
        value, error = parse_int(raw)
        print(f"parse_int({raw!r}) -> value={value} error={error}")

    for numerator, denominator in ((10, 4), (10, 0)):
        value, error = divide(numerator, denominator)
        print(f"divide({numerator}, {denominator}) -> value={value} error={error}")

    for path in (__file__, "does_not_exist.txt"):
        contents, error = read_file(path)
        length = None if contents is None else len(contents)
        print(f"read_file -> chars={length} error={error}")

        contents, error = read_file_manual(path)
        length = None if contents is None else len(contents)
        print(f"read_file_manual -> chars={length} error={error}")

    for raw in ("42", "abc"):
        print(f"clause order for {raw!r}: {' -> '.join(trace_clause_order(raw))}")


if __name__ == "__main__":
    main()