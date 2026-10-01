from pathlib import Path
from walk_a_directory import directory
import hashlib

def hash_directory(root: Path) -> dict[str, str]:
    hashes = {}
    for item in directory(root):
        if item.is_file():
            file_hash = hashlib.sha256(item.read_bytes()).hexdigest()
            hashes[str(item.relative_to(root))] = file_hash
    return hashes

if __name__ == "__main__":
    sandbox = Path(__file__).parent / "sandbox"
    for key, value in hash_directory(sandbox).items():
        print(f"{key}: {value}")

# import hashlib
# from pathlib import Path

# from walk_a_directory import directory

# CHUNK_SIZE = 64 * 1024


# def hash_file(path: Path) -> str:
#     digest = hashlib.sha256()
#     with path.open("rb") as f:
#         while chunk := f.read(CHUNK_SIZE):
#             digest.update(chunk)
#     return digest.hexdigest()


# def hash_directory(root: Path) -> dict[str, str]:
#     hashes: dict[str, str] = {}
#     for item in directory(root):
#         if item.is_file():
#             hashes[item.relative_to(root).as_posix()] = hash_file(item)
#     return hashes


# if __name__ == "__main__":
#     sandbox = Path(__file__).parent / "sandbox"
#     for relative_path, file_hash in hash_directory(sandbox).items():
#         print(f"{relative_path}: {file_hash}")