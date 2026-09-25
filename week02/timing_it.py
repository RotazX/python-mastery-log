import time

def linear_search(arr: list[int], nr: int) -> int:
    print("inside linear_search")
    for i, v in enumerate(arr):
        if v == nr:
            return i
    return -1

def binary_search(arr: list[int], nr: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == nr:
            return mid
        if arr[mid] < nr:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    numbers = [x for x in range(100_000)]

    start = time.perf_counter()
    v = linear_search(numbers, 90_000)
    print(v)
    elapsed = time.perf_counter() - start
    print(f"Linear search time spent: {elapsed:.15f} s")

    start2 = time.perf_counter()
    v2 = binary_search(numbers, 90_000)
    print(v2)
    elapsed2 = time.perf_counter() - start2
    print(f"Binary search time spent: {elapsed2:.15f} s")

    # print(binary_search(numbers, 4))
    # print(binary_search(numbers, 42))
    
    