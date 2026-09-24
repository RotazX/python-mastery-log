import time

def linear_search(arr: list[int], nr: int) -> int:
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
    print(linear_search([4, 8, 15, 16, 23, 42], 23))
    print(linear_search([4, 8, 15, 16, 23, 42], 7))

    print(binary_search([4, 8, 15, 16, 23, 42], 23))
    print(binary_search([4, 8, 15, 16, 23, 42], 7))
    print(binary_search([4, 8, 15, 16, 23, 42], 4))
    print(binary_search([4, 8, 15, 16, 23, 42], 42))