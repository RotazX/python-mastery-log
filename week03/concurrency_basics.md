The GIL in plain terms

The Global Interpreter Lock (GIL) is a lock inside CPython (the standard Python). It lets only one thread run Python bytecode at a time, even on a multi-core machine. It exists because CPython's memory management, especially reference counting, isn't thread-safe on its own. One big lock is simpler and faster for single-threaded code than many small locks.

The key detail is that a thread releases the GIL while it waits on I/O: reading or writing a file, waiting on the disk, or waiting on the network. While one thread waits, another can take the GIL and run.

I/O-bound work: most of the time is spent waiting, and threads take turns cleanly. Ten threads can have ten disk or network operations in flight at once, so you get real speedup.
CPU-bound work (heavy math, image processing, pure-Python loops): threads compete for the one lock and effectively run one at a time. You get little or no speedup, sometimes a slowdown from switching overhead. For that kind of work, use multiprocessing or ProcessPoolExecutor, where each process has its own GIL.

Mental model: the GIL is one microphone. Only one thread can talk at a time, but a thread waiting for the disk doesn't need the mic, so it hands it over.

Why a directory synchronizer fits threading

A sync tool mostly does I/O-bound work: it stats files, reads them to hash, copies bytes, and writes to the destination. Each of those operations spends most of its time waiting on the disk, and during that wait the thread releases the GIL. So a thread pool keeps several file operations in flight at once instead of handling them strictly one after another, which hides the latency.

There's one caveat. Hashing is partly CPU work, but hashlib releases the GIL while hashing large buffers, and disk reads usually dominate anyway. The workload is therefore mostly waiting, which is exactly the case threading is good at.

One-liner: threads don't make Python compute faster, they make it wait in parallel, and a sync tool is mostly waiting.