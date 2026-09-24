
def bubble_sort(numbers: list[int]) -> list[int]:
    result = numbers.copy()
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


if __name__ == "__main__":
    arr = [5, 2, 9, 1, 7, 3]
    result = bubble_sort(arr)
    print(result)
    print(result == sorted(arr))
    print(arr)