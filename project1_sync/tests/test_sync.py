from pathlib import Path

def test_two_paths_exist(tmp_path: Path) -> None:
    source = tmp_path / "source"
    source.mkdir()
    destination = tmp_path / "destination"
    destination.mkdir()
    assert source.exists()
    assert destination.exists()