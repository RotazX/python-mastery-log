"""
Compare two large files in two different ways and measure time + memory.

  Method A: read BOTH files fully into memory, then compare byte-for-byte (a == b)
  Method B: hash each file in small chunks (SHA-256), then compare the hashes

Uses: time (speed), hashlib (hashing), pathlib (files),
      tracemalloc (built-in, measures peak memory Python used).
"""

import hashlib
import os
import time
import tracemalloc
from pathlib import Path

# ---------- settings ----------
FILE_SIZE_MB = 200            # size of each test file
CHUNK_SIZE = 1024 * 1024      # read 1 MB at a time when hashing
FOLDER = Path("test_files")
FILE_A = FOLDER / "file_a.bin"
FILE_B = FOLDER / "file_b.bin"


# ---------- step 1: create two identical big files ----------
def make_test_files() -> None:
    FOLDER.mkdir(exist_ok=True)
    target = FILE_SIZE_MB * 1024 * 1024

    if FILE_A.exists() and FILE_A.stat().st_size == target and FILE_B.exists():
        print(f"Using existing test files ({FILE_SIZE_MB} MB each)\n")
        return

    print(f"Creating two {FILE_SIZE_MB} MB test files...")
    with FILE_A.open("wb") as a, FILE_B.open("wb") as b:
        written = 0
        while written < target:
            chunk = os.urandom(CHUNK_SIZE)   # random bytes
            a.write(chunk)
            b.write(chunk)                   # same bytes -> identical files
            written += len(chunk)
    print("Done.\n")


# ---------- method A: load everything into memory ----------
def compare_in_memory(path1: Path, path2: Path) -> bool:
    data1 = path1.read_bytes()   # whole file 1 in RAM
    data2 = path2.read_bytes()   # whole file 2 in RAM
    return data1 == data2


# ---------- method B: hash in chunks ----------
def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(CHUNK_SIZE):   # only 1 MB in RAM at a time
            h.update(chunk)
    return h.hexdigest()


def compare_by_hash(path1: Path, path2: Path) -> bool:
    return hash_file(path1) == hash_file(path2)


# ---------- measuring helper ----------
def measure(name: str, func, *args):
    tracemalloc.start()
    start = time.perf_counter()

    result = func(*args)

    elapsed = time.perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    peak_mb = peak / (1024 * 1024)
    print(f"{name}")
    print(f"  files equal : {result}")
    print(f"  time        : {elapsed:.3f} s")
    print(f"  peak memory : {peak_mb:.1f} MB\n")
    return elapsed, peak_mb


# ---------- main ----------
def main() -> None:
    make_test_files()

    t_a, m_a = measure("Method A - read both fully + compare", compare_in_memory, FILE_A, FILE_B)
    t_b, m_b = measure("Method B - SHA-256 in 1 MB chunks", compare_by_hash, FILE_A, FILE_B)

    print("=" * 50)
    faster = "A (in-memory)" if t_a < t_b else "B (hashing)"
    print(f"Faster: Method {faster}")
    print(f"Memory: A used {m_a:.1f} MB, B used {m_b:.1f} MB "
          f"(~{m_a / max(m_b, 0.01):.0f}x less with hashing)")
    print("""
Why it matters:
  Method A needs RAM equal to BOTH files combined. Two 10 GB files
  would need ~20 GB of RAM -> the program slows to a crawl or crashes.
  Method B only ever holds one 1 MB chunk, so it works the same on a
  10 MB file or a 100 GB file. Memory use stays flat no matter the size.
""")


if __name__ == "__main__":
    main()