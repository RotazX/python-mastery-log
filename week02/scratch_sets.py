
def common_friends(friends1: list[str], friends2: list[str]) -> set[str]:
    s1 = set(friends1)
    s2 = set(friends2)
    if not friends2 or not friends1:
        return []
    else:
        return s1 & s2

def all_friends(friends1: list[str], friends2: list[str]) -> set[str]:
    s1 = set(friends1)
    s2 = set(friends2)
    # s = s1.update(s2)
    return s1 | s2

def friends_only_in_first(friends1: list[str], friends2: list[str]) -> set[str]:
    s1 = set(friends1)
    s2 = set(friends2)
    return s1 - s2

def friends_in_exactly_one(friends1: list[str], friends2: list[str]) -> set[str]:
    s1 = set(friends1)
    s2 = set(friends2)
    return s1 ^ s2

if __name__ == "__main__":
    first = ["Anna", "Bob", "Carla", "Carla"]
    second = ["Carla", "Dan", "Anna"]

    print(sorted(common_friends(first, second)))
    print(sorted(all_friends(first, second)))
    print(sorted(friends_only_in_first(first, second)))
    print(sorted(friends_only_in_first(second, first)))
    print(sorted(friends_in_exactly_one(first, second)))
    print(common_friends(first, []))