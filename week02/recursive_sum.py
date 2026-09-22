
def recursive_sum(nums: list[int]) -> int:
    if not nums:
        return 0
    else:
        return nums[0] + recursive_sum(nums[1:])

def count_items(nested: list[object]) -> int:
    total = 0
    # The loop goes across this level; the recursion goes down into sublists.
    for element in nested:
        if isinstance(element, list):
            # Recursive case: a sublist contributes however many items it contains.
            total += count_items(element)
        else:
            # Base case: a non-list element is one item, with nothing deeper to explore.
            total += 1
    return total


def main() -> None:
    while True:
        q = input("Write a list of numbers! ")
        try:
            numbers = [int(i) for i in q.split()]
            break
        except ValueError:
            print("You have not entered only numbers. Please try again. \n")

    print(f"The sum of the numbers is {recursive_sum(numbers)}.")

    test_cases: list[list[object]] = [
        [],
        [1, 2, 3],
        [1, [2, 3], [[4]], []],
        [[[[]]]],
    ]
    for case in test_cases:
        print(f"count_items({case}) = {count_items(case)}")


if __name__ == "__main__":
    main()
