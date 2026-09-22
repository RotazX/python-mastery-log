
people = [
    {"name": "Ana", "age": 31, "score": 88},
    {"name": "Marko", "age": 24, "score": 72},
    {"name": "Liis", "age": 31, "score": 95},
    {"name": "Toomas", "age": 19, "score": 64},
    {"name": "Kert", "age": 24, "score": 81},
]

def sort_by_age(people: list[dict]) -> list[dict]:
    return sorted(people, key=lambda n: n["age"], reverse=False)

def sort_by_score_desc(people: list[dict]) -> list[dict]:
    return sorted(people, key=lambda n: n["score"], reverse=True)

def filter_above(people: list[dict], threshold: int) -> list[dict]:
    return list(filter(lambda s: s["score"] > threshold, people))

def get_names(people: list[dict]) -> list[str]:
    return list(map(lambda n: n["name"], people))

def sort_by_age_then_name(people: list[dict]) -> list[dict]:
    return sorted(people, key=lambda n: (n["age"], len(n["name"])))

# the list-comprehension versions:

def filter_above_lc(people: list[dict], threshold: int) -> list[dict]:
    return [p for p in people if p["score"] > threshold]

def get_names_lc(people: list[dict]) -> list[str]:
    return [p["name"] for p in people]

if __name__ == "__main__":
    print(sort_by_age(people))
    print(sort_by_score_desc(people))
    print(filter_above(people, 80))
    print(get_names(people))
    print(sort_by_age_then_name(people))