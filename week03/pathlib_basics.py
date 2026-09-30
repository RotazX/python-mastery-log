from pathlib import Path

# def describe_path(path: Path) -> None:
#     print(path.exists())
#     print(path.is_file())
#     print(path.is_dir())
#     # for file_path in path.glob("*.txt"):
#     #     with open(file_path, "r", encoding="utf-8") as file:
#     #         content = file.read()
#     #         print(file_path.name)
#     #         print(content)
#     for file_path in path.glob("*.txt"):
#          print(file_path)

#     for file_path in path.rglob("*"):
#             print(file_path)

# if __name__ == "__main__":
#     describe_path(Path("sandbox"))
#     describe_path(Path("s"))

def path_info(path: Path) -> dict[str, bool]:
    return {"exists": path.exists(), "is_file": path.is_file(), "is_dir": path.is_dir()}


def top_level_txt_files(path: Path) -> list[Path]:
    return sorted(path.glob("*.txt"))


def everything_below(path: Path) -> list[Path]:
    return sorted(path.rglob("*"))


def print_report(path: Path) -> None:
    print(f"--- {path} ---")
    for label, value in path_info(path).items():
        print(f"{label}: {value}")
    print("glob('*.txt'):")
    for item in top_level_txt_files(path):
        print(f"  {item}")
    print("rglob('*'):")
    for item in everything_below(path):
        print(f"  {item}")

if __name__ == "__main__":
    for target in [Path("sandbox"), Path("does_not_exist")]:
        print_report(target)
