from pathlib import Path

def read_lines(path: Path) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip("\n") for line in f]

def count_words(lines: list[str]) -> int:
   return sum(len(line.split()) for line in lines)

def longest_line(lines: list[str]) -> str:
    return max(lines, key=len, default="")

if __name__ == "__main__":
    lines = read_lines(Path(__file__).parent / "sample.txt")
    print(count_words(lines))
    print(longest_line(lines))
    print(longest_line([]))