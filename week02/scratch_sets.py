
def common_friends(friends1: list[str], friends2: list[str]) -> set[str]:
    if not friends1 or not friends2:
        return []
    else:
        return set(friends1) & set(friends2)
    
def all_friends(friends1: list[str], friends2: list[str]) -> set[str]:
    return set(friends1) | set(friends2)

def friends_only_in_first(friends1: list[str], friends2: list[str]) -> set[str]:
    return set(friends1) - set(friends2)

def friends_in_exactly_one(friends1: list[str], friends2: list[str]) -> set[str]:
    return set(friends1) ^ set(friends2)

if __name__ == "__main__":
    first = ["Anna", "Bob", "Carla", "Carla"]
    second = ["Carla", "Dan", "Anna"]

    print(sorted(common_friends(first, second)))
    print(sorted(all_friends(first, second)))
    print(sorted(friends_only_in_first(first, second)))
    print(sorted(friends_only_in_first(second, first)))
    print(sorted(friends_in_exactly_one(first, second)))
    print(common_friends(first, []))