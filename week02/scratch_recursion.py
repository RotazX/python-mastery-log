
def count_items(lists: list[int]) -> int:
    count = 0
    if len(lists) == 0:
        return count
    else: 
        for i in lists:
            if isinstance(i, int):
                count += 1
            else:
                count = count + count_items(i)
        return count

if __name__ == "__main__":
    lists = [1, [2, 3], [[4]], 6]
    lists2 = [[[3]]]

    print(count_items(lists2))