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
    hash_a = file_hash(path_a)
    hash_b = file_hash(path_b)

    if hash_a == hash_b:
        return bool(True)
    else:
        return bool(False)



if __name__ == "__main__":
    print("Files are identical:", files_are_identical(Path("a.txt"), Path("b.txt")))