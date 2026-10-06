from pathlib import Path
from diff import compute_sync_plan

def execute_sync_plan(
    plan: dict[str, set[Path]],
    source: Path,
    dest: Path,
    dry_run: bool = True
) -> None:
    for path in plan["copy"]:
        source_path = source / path
        dest_path = dest / path
        print(f"COPY {source_path} -> {dest_path}")

    for path in plan["update"]:
        print(f"UPDATE {path}")

    for path in plan["delete"]:
        print(f"DELETE {path}")

if __name__ == "__main__":
    path = Path(__file__).parent

    plan = compute_sync_plan(
        path / "test_src",
        path / "test_dst"
    )

    print(plan)

    execute_sync_plan(
    plan,
    path / "test_src",
    path / "test_dst"
    )