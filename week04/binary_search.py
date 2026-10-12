
def binary_search(arr: list[int], target: int) -> int | None:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1

    return None

if __name__ == "__main__":
    print(binary_search([x for x in range(1000)], 823))