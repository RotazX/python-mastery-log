"""Linear search vs binary search on a sorted list."""


def linear_search(items: list[int], target: int) -> int | None:
    """Return the index of target, checking every element in order. O(n)."""
    for index, value in enumerate(items):
        if value == target:
            return index
    return None


def binary_search(items: list[int], target: int) -> int | None:
    """Return the index of target in a sorted list, halving the range each step. O(log n)."""
    # WHY THE LIST MUST BE SORTED:
    # Each step compares the target to the middle element and discards half
    # of the remaining range. Discarding is only safe because sorting guarantees
    # that everything left of mid is <= items[mid] and everything right is >=.
    # On an unsorted list that guarantee is gone: the discarded half can contain
    # the target, and the function silently returns None for a value that is
    # actually present. It does not crash, it just gives a wrong answer.
    low = 0
    high = len(items) - 1

    while low <= high:  # <= so the last remaining candidate still gets checked
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1  # mid is already ruled out, so skip past it
        else:
            high = mid - 1  # same reasoning on the other side

    return None


def compare_searches(
    items: list[int], targets: list[int]
) -> list[tuple[int, int | None, int | None]]:
    """Run both searches for each target and return (target, linear, binary) rows."""
    return [(t, linear_search(items, t), binary_search(items, t)) for t in targets]


if __name__ == "__main__":
    sorted_items = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    # first element, last element, a middle element, a missing value
    targets = [1, 19, 11, 4]

    print("Sorted list:", sorted_items)
    for target, lin, bin_ in compare_searches(sorted_items, targets):
        print(f"  target={target:>2}  linear={lin}  binary={bin_}")

    unsorted_items = [7, 3, 9, 1, 5]
    print("\nUnsorted list:", unsorted_items)
    for target, lin, bin_ in compare_searches(unsorted_items, [3]):
        print(f"  target={target:>2}  linear={lin}  binary={bin_}  <- binary is wrong: 3 is at index 1")