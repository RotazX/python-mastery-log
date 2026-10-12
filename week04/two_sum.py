
def brute_force(items: list[int], target: int) -> tuple[int, int] | None: # O(n^2)
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] + items[j] == target:
                return i, j
    return None

def linear_force(items: list[int], target: int) -> tuple[int, int] | None: # O(n)
    seen = {}
    for i, num in enumerate(items):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return None

    

if __name__ == "__main__":
    l = [3, 3]
    print(brute_force(l, 6))
    print(linear_force(l, 6))