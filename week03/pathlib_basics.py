from pathlib import Path

def describe_path(path: Path) -> None:
    print(path.exists())
    print(path.is_file())
    print(path.is_dir())
    # for file_path in path.glob("*.txt"):
    #     with open(file_path, "r", encoding="utf-8") as file:
    #         content = file.read()
    #         print(file_path.name)
    #         print(content)
    for file_path in path.glob("*.txt"):
         print(file_path)
         
    for file_path in path.rglob("*"):
            print(file_path)

if __name__ == "__main__":
    describe_path(Path("sandbox"))
    describe_path(Path("s"))
