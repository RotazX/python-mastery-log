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
    path = Path(__file__).parent
    for key, value in hash_directory(path / "sandbox").items():
        print(f"{key}: {value}")