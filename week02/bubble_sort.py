
def bubble_sort(numbers: list[int]) -> list[int]:
    n = len(numbers)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers

def sort(numbers: list[int]) -> list[int]:
    return sorted(numbers, reverse=False)


if __name__ == "__main__":
    if bubble_sort([5, 2, 9, 1, 7, 3]) == sort([5, 2, 9, 1, 7, 3]):
        print("True")
    else:
        print("False")
    
    print(bubble_sort([5, 2, 9, 1, 7, 3])) 
    print(sort([5, 2, 9, 1, 7, 3]))
    