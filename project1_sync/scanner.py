from pathlib import Path

def scan_directory(path: Path) -> list[Path]:
    return [p for p in path.rglob("*") if p.is_file()]

def safe_resolve(base: Path, target: Path) -> Path:
    resolved_base = base.resolve()
    
    if target.is_absolute():
        resolved_target = target.resolve()
    else:
        resolved_target = (resolved_base / target).resolve()

    if not resolved_target.is_relative_to(resolved_base):
        raise ValueError(f"'{target}' escapes the base folder")
        
    return resolved_target
