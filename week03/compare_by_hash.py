from pathlib import Path
import hashlib

CHUNK_SIZE = 65536

def file_hash(file_path: Path) -> str:
    path = Path(__file__).parent / "sandbox"
    hasher = hashlib.new("sha256")
    with open(path / file_path, "rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            hasher.update(chunk)
    return hasher.hexdigest()


def files_are_identical(path_a: Path, path_b: Path) -> bool:
    return file_hash(path_a) == file_hash(path_b)




if __name__ == "__main__":
    sandbox = Path(__file__).parent / "sandbox"
    result = files_are_identical(sandbox / "a.txt", sandbox / "b.txt")
    print(f"Files are identical: {result}")