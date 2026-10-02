from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import time


def fake_io(name: str, seconds: int, start: float) -> None:
    print(f"{name} start: {time.perf_counter() - start:.2f}s")
    time.sleep(seconds)
    print(f"{name} end: {time.perf_counter() - start:.2f}s")


def run_sequential(tasks: list[tuple[str, int]]) -> float:
    start = time.perf_counter()
    for name, seconds in tasks:
        fake_io(name, seconds, start)
    return time.perf_counter() - start


def run_with_threads(tasks: list[tuple[str, int]]) -> float:
    start = time.perf_counter()
    threads = []
    for name, seconds in tasks:
        threads.append(Thread(target=fake_io, args=(name, seconds, start)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.perf_counter() - start


def run_with_pool(tasks: list[tuple[str, int]]) -> float: # I/O-bound: threading helps because threads can overlap waiting during sleep.
    start = time.perf_counter()
    futures = []
    with ThreadPoolExecutor() as pool:
        for name, seconds in tasks:
            futures.append(pool.submit(fake_io, name, seconds, start))
    for future in futures:
        future.result()  # re-raises any exception that happened inside the task
    return time.perf_counter() - start


if __name__ == "__main__":
    tasks = [("A", 2), ("B", 3)]

    print("--- sequential ---")
    print(f"Total: {run_sequential(tasks):.2f}s")

    print("--- threaded ---")
    print(f"Total: {run_with_threads(tasks):.2f}s")

    print("--- pool ---")
    print(f"Total: {run_with_pool(tasks):.2f}s")