from pathlib import Path

def test_machine(tmp_path) -> None:
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("hello")
    assert p.read_text(encoding="utf-8") == "hello"
    