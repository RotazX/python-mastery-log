import sys

def main(path: str) -> None:
    print(f"Average score was {average_score(parse_scores(read_lines(path))):.2f}")
    print("")
    print("Leaderboard:")
    for position, (name, score) in enumerate(leaderboard(parse_scores(read_lines(path))), start=1):
        print(f"  {position}. {name:<10} {score}")
    print("")
    print(f"Top scorers were:")
    for i in top_n(leaderboard(parse_scores(read_lines(path)))): print(i)


def read_lines(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()

def parse_scores(lines: list[str]) -> dict[str, int]:
    scores = {}
    for line in lines:
        line = line.strip().split(",")
        if len(line) == 2 and line[0] != "":
            try:
                score = int(line[1].strip())
                scores[line[0].strip()] = score
            except ValueError:
                continue
        else:
            continue
    return scores

def average_score(scores: dict[str, int]) -> float:
    numbers = []
    for score in scores.values():
        numbers.append(score)
    return (sum(numbers) / len(numbers))

def leaderboard(scores: dict[str, int]) -> list[tuple[str, int]]:
        return sorted(scores.items(), key=lambda pair: pair[1], reverse=True)

def top_n(scores: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return scores[:3]

if __name__ == "__main__":
    main(sys.argv[1])

