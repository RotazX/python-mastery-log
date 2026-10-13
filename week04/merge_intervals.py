
def merge_intervals(numbers: list[tuple[int, int]]) -> list[tuple[int, int]]:
    numbers = sorted(numbers, key=lambda number: number[0])
    merged = []
    for i in numbers:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else: 
            merged[-1] = (merged[-1][0], max(merged[-1][1], i[1]))
    return merged
    
if __name__ == "__main__":
    test_cases = [
        [],
        [(5, 7)],
        [(1, 2), (4, 5)],
        [(1, 4), (3, 6), (5, 8)],
        [(1, 10), (2, 3), (10, 12)],
        [(8, 10), (1, 3), (2, 6)],
        [(6, 9), (1, 10)],
        [(2, 3), (2, 3)]
    ]
    for num in test_cases:
        print(merge_intervals(num))