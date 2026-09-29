
people = [
    {"name": "Anna", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Carla", "score": 91},
]

def filter_above(people: list[dict], threshold: int) -> list[dict]:
    return list(filter(lambda p: p["score"] > threshold, people))

def filter_above_lc(people: list[dict], threshold: int) -> list[dict]:
    return [p for p in people if p["score"] > threshold]

def get_names(people: list[dict]) -> list[str]:
    return list(map(lambda p: p["name"], people))

def get_names_lc(people: list[dict]) -> list[str]:
    return [p["name"] for p in people]

if __name__ == "__main__":
    print(filter_above(people, 80))
    print(filter_above_lc(people, 80))
    print(filter_above(people, 100))
    print(filter_above_lc(people, 100))
    print(get_names(people))
    print(get_names_lc(people))