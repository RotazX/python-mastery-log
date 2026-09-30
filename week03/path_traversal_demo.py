from pathlib import Path

def safe_join(base: Path, user_input: str) -> Path:
    resolved_base = base.resolve()
    resolved_target = (resolved_base / user_input).resolve()

    if not resolved_target.is_relative_to(resolved_base):
        raise ValueError(f"'{user_input}' escapes the base folder")
    return resolved_target

if __name__ == "__main__":
    base = Path(__file__).parent / "sandbox"

    print(safe_join(base, "notes.txt"))

    try:
        safe_join(base, "../../etc/passwd")
    except ValueError as e:
        print("Blocked:", e)