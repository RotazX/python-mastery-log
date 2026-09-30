from pathlib import Path

def test_machine(tmp_path: Path) -> None:
    p = tmp_path / "hello.py"
    p.write_text("hello")
    assert p.read_text(encoding="utf-8") == "hello"
    