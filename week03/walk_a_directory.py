from pathlib import Path

def directory(path: Path) -> list[Path]:
    return sorted(path.rglob("*"))

if __name__ == "__main__":
    print(directory(Path("sandbox")))
    for item in directory(Path("sandbox")):
        if item.is_file():
            print(f"{item}: {item.stat().st_size}")
        
