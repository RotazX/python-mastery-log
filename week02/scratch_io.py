from pathlib import Path

def read_lines(path: Path) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip("\n") for line in f]

def count_words(lines: list[str]) -> int:
    count = 0
    for line in lines:
        count += int(len(line.split()))
    return count



def longest_line(lines: list[str]) -> str:
    if not lines:
        return ""
    else:
        sorted_lines = sorted(lines, key=lambda x: len(x), reverse=True)
        return sorted_lines[0]

if __name__ == "__main__":
    lines = read_lines(Path("sample.txt"))
    print(count_words(lines))
    print(longest_line(lines))
    print(longest_line([]))