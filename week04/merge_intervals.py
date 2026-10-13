
def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[tuple[int, int]] = []
    for start, end in sorted(intervals):
        if not merged or merged[-1][1] < start:
            merged.append((start, end))
        else: 
            last_start, last_end = merged[-1]
            merged[-1] = (last_start, max(last_end, end))
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