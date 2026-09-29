
def count_items(lists: list) -> int:
    count = 0
    # if len(lists) == 0: This is not 
    #     return count
    # else: 
    for i in lists:
        if isinstance(i, list): # If class is int then with float the program crashes, and with a string you will get a recursion error.
            count += 1
        else:
            count = count + count_items(i)
    return count

if __name__ == "__main__":
    lists = [1, [2, 3], [[4]], 6]
    lists2 = [[[3]]]

    print(count_items(lists2))