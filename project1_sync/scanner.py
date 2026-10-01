from fnmatch import fnmatch
from pathlib import Path


def is_excluded(relative: Path, patterns: list[str]) -> bool:
    return any(fnmatch(part, pattern) for part in relative.parts for pattern in patterns)


def scan_directory(path: Path, exclude_patterns: list[str] | None = None) -> list[Path]:
    if exclude_patterns is None:
        exclude_patterns = []
    return [
        p for p in path.rglob("*")
        if p.is_file() and not is_excluded(p.relative_to(path), exclude_patterns)
    ]


def safe_resolve(base: Path, target: Path) -> Path:
    resolved_base = base.resolve()
    if target.is_absolute():
        resolved_target = target.resolve()
    else:
        resolved_target = (resolved_base / target).resolve()
    if not resolved_target.is_relative_to(resolved_base):
        raise ValueError(f"'{target}' escapes the base folder")
    return resolved_target