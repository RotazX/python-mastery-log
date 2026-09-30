from pathlib import Path

def safe_join(base: Path, user_input: str) -> Path:
    resolved_base = Path(base).resolve()
    resolved_target = Path(resolved_base / user_input).resolve()

    if resolved_target.is_relative_to(resolved_base):
        return resolved_target
    raise ValueError(f"Path '{resolved_target}' is outside the base folder '{resolved_base}'.")

if __name__ == "__main__":
    print(safe_join("sandbox", "notes.txt"))
    
    try:
        print(safe_join("sandbox", "../../etc/passwd"))
    except ValueError as e:
        print("Caught expected error:", e)