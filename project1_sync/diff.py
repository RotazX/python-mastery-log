from pathlib import Path
import scanner
import hashlib

def hash_file(path: Path) -> str:
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()

def build_hash_map(root: Path) -> dict[Path, str]:
    files = {}

    for p in scanner.scan_directory(root):
        relative_path = p.relative_to(root)
        files[relative_path] = hash_file(p)

    return files
    
def compute_sync_plan(source: Path, dest: Path) -> dict:
    # Build a hash map for the source directory and a hash map for the destination directory.
    #
    # Copied: go through files in the source. If a file is not in the destination,
    # it needs to be copied.
    #
    # Updated: go through files that exist in both source and destination.
    # If their hashes are different, the source file needs to update the destination file.
    #
    # Deleted: go through files in the destination. If a file is not in the source,
    # it needs to be deleted.
    #
    # Unchanged: go through files that exist in both source and destination.
    # If their hashes are the same, nothing needs to happen.
    #
    # Return a dictionary whose keys are the four category names:
    # copied, updated, deleted, and unchanged.
    # Each key holds a collection of relative file paths belonging to that category.
    source_files = build_hash_map(source)
    dest_files = build_hash_map(dest)

    plan = {
        "copy": set(),
        "update": set(),
        "delete": set(),
        "unchanged": set(),
    }

    for path, source_hash in source_files.items():
        if path not in dest_files:
            plan["copy"].add(path)
        elif source_hash != dest_files[path]:
            plan["update"].add(path)
        else:
            plan["unchanged"].add(path)

    for path in dest_files:
        if path not in source_files:
            plan["delete"].add(path)

    return plan

if __name__ == "__main__":
    path = Path(__file__).parent 

    source_files = build_hash_map(path / "test_src")
    dest_files = build_hash_map(path / "test_dst")

    print("Source:", source_files)
    print("Dest:", dest_files)

    print("Sync Plan:", compute_sync_plan(
        path / "test_src",
        path / "test_dst"
    ))