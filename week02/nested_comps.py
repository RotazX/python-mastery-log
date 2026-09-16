
lists = [[1, 2, 3], [4, 5], [6]]

def flatten(list_of_lists: list[list]) -> list:
    return [item for list in list_of_lists for item in list]

print(flatten(lists))

