from pathlib import Path
import pytest
from project1_sync.scanner import safe_resolve, scan_directory

def test_scan_excludes_hidden_and_tmp_files(tmp_path: Path) -> None:
    normal = tmp_path / "notes.txt"
    hidden = tmp_path / ".secret"
    temp = tmp_path / "draft.tmp"
    for f in (normal, hidden, temp):
        f.write_text("x")

    result = scan_directory(tmp_path, exclude_patterns=["*.tmp", ".*"])

    assert normal in result
    assert hidden not in result
    assert temp not in result

def test_scan_excludes_files_inside_hidden_folders(tmp_path: Path) -> None:
    hidden_dir = tmp_path / ".git"
    hidden_dir.mkdir()
    inside = hidden_dir / "config"
    inside.write_text("x")

    result = scan_directory(tmp_path, exclude_patterns=[".*"])

    assert inside not in result