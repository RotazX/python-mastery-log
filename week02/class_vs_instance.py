
class Counter:
    total_counters_created: int = 0  # class attribute: one shared copy

    def __init__(self) -> None:
        self.count: int = 0  # instance attribute: each object gets its own
        Counter.total_counters_created += 1

    def increment(self) -> None:
        self.count += 1


if __name__ == "__main__":
    counter_a = Counter()
    counter_b = Counter()
    counter_c = Counter()

    counter_a.increment()

    counter_b.increment()
    counter_b.increment()
    counter_b.increment()

    print(f"counter_a.count: {counter_a.count}")
    print(f"counter_b.count: {counter_b.count}")
    print(f"counter_c.count: {counter_c.count}")
    print(f"Counter.total_counters_created: {Counter.total_counters_created}")