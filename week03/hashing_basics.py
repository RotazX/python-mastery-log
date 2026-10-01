import hashlib
from pathlib import Path

CHUNK_SIZE = 65536  # 64 KiB per read


def hash_bytes(data: bytes, algorithm: str) -> str:
    return hashlib.new(algorithm, data).hexdigest()


def hash_string(text: str, algorithm: str) -> str:
    return hash_bytes(text.encode("utf-8"), algorithm)


def hash_file(file_path: Path, algorithm: str) -> str:
    hasher = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            hasher.update(chunk)
    return hasher.hexdigest()


if __name__ == "__main__":
    hello_file = Path(__file__).parent / "hello.txt"

    cases = [
        ("sha256 'hello'", hash_string("hello", "sha256"),
         "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"),
        ("sha256 ''", hash_string("", "sha256"),
         "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
        ("md5 'hello'", hash_string("hello", "md5"),
         "5d41402abc4b2a76b9719d911017c592"),
        ("md5 ''", hash_string("", "md5"),
         "d41d8cd98f00b204e9800998ecf8427e"),
        ("sha256 hello.txt", hash_file(hello_file, "sha256"),
         "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"),
        ("md5 hello.txt", hash_file(hello_file, "md5"),
         "5d41402abc4b2a76b9719d911017c592"),
    ]

    for label, actual, expected in cases:
        status = "OK  " if actual == expected else "FAIL"
        print(f"{status} {label}")