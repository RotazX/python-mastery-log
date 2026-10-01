import pytest
from pathlib import Path
from project1_sync.scanner import safe_resolve
from project1_sync.scanner import scan_directory


def test_safe_resolve_blocks_escape(tmp_path: Path):
    # Setup a sandbox base directory
    base_dir = tmp_path / "sandbox"
    base_dir.mkdir()
    
    # 1. Test valid path inside the base folder
    valid_target = Path("notes.txt")
    expected_path = base_dir / "notes.txt"
    assert safe_resolve(base_dir, valid_target) == expected_path
    
    # 2. Test relative path escape attempt using '../'
    escape_target_relative = Path("../../etc/passwd")
    with pytest.raises(ValueError, match="escapes the base folder"):
        safe_resolve(base_dir, escape_target_relative)

    # 3. Test absolute path escape attempt
    escape_target_absolute = Path("/etc/passwd")
    with pytest.raises(ValueError, match="escapes the base folder"):
        safe_resolve(base_dir, escape_target_absolute)

def test_scan_excludes_hidden_and_tmp_files(tmp_path):
    normal = tmp_path / "notes.txt"
    hidden = tmp_path / ".secret"
    temp = tmp_path / "draft.tmp"
    for f in (normal, hidden, temp):
        f.write_text("x")
 
    result = scan_directory(tmp_path, exclude_patterns=["*.tmp", ".*"])
 
    assert normal in result
    assert hidden not in result
    assert temp not in result
