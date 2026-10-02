from threading import Thread, Lock
import time

def run_without_lock(increments: int) -> int: # CPU-bound: threading does not meaningfully speed up the work because of Python's GIL.
    counter = [0]

    def worker() -> None:
        for _ in range(increments):
            value = counter[0]
            time.sleep(0)
            counter[0] = value + 1

    t1 = Thread(target=worker)
    t2 = Thread(target=worker)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return counter[0]

def run_with_lock(increments: int) -> int: # CPU-bound: threading does not meaningfully speed up the work because of Python's GIL.
    counter = [0]
    lock = Lock()

    def worker() -> None:
        for _ in range(increments):
            with lock:
                value = counter[0]
                time.sleep(0)
                counter[0] = value + 1

    t1 = Thread(target=worker)
    t2 = Thread(target=worker)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return counter[0]

if __name__ == "__main__":
    print(run_without_lock(1_000_000))
    print(run_with_lock(1_000_000))