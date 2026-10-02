import time
from threading import Thread

def fake_io(name: str, s: int, start: float) -> None: # I/O-bound: threading helps because threads can overlap waiting during sleep.
    print(f"{name} start: {time.perf_counter() - start:.2f}s")
    time.sleep(s)
    print(f"{name} end: {time.perf_counter() - start:.2f}s")

if __name__ == "__main__":
    start = time.perf_counter()
    t = Thread(target=fake_io, args=("A", 2, start))
    t2 = Thread(target=fake_io, args=("B", 3, start))

    print("--- sequential ---")
    fake_io("A", 2, start)
    fake_io("B", 3, start)
    print(f"Total: {time.perf_counter() - start:.2f}")

    start2 = time.perf_counter()
    t3 = Thread(target=fake_io, args=("A", 2, start2))
    t4 = Thread(target=fake_io, args=("B", 3, start2))

    print("--- threaded ---")
    t3.start()
    t4.start()
    
    t3.join()
    t4.join()
    print(f"Total: {time.perf_counter() - start2:.2f}")
    

