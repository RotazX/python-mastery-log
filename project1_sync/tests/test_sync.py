from pathlib import Path

def test_two_paths_exist(tmp_path: Path) -> None:
    source = tmp_path / "source"
    destination = tmp_path / "destination"

    source.mkdir()
    destination.mkdir()

    assert source.is_dir()
    assert destination.is_dir()