Hash comparison vs. full-content comparison

Why hashing scales better: Comparing full contents means reading both files byte by byte every time you compare them. With N files, finding duplicates by pairwise comparison takes about N² comparisons. A hash reduces each file to a short fixed-size fingerprint (32 bytes for SHA-256). You read each file once, store its hash, and then compare tiny strings or look them up in a dict. That turns duplicate-finding into a single O(N) pass. The hashes can also be cached, so a file only needs re-reading if its size or modification time changed.

Cheap pre-filter: Files of different sizes can't be identical. Check size first, and only hash files whose sizes match.

SHA-256 vs. MD5

MD5 is fast and fine for casual deduplication. Two random files colliding by accident is essentially impossible. The problem is that MD5 is broken against deliberate attacks: someone can craft two different files with the same MD5 hash on purpose. So MD5 is unsafe for anything where an attacker could be involved, like verifying downloads, detecting tampering, or checking backups you need to trust. SHA-256 has no known practical collisions and is the default whenever integrity actually matters. It's a bit slower, but disk speed is usually the bottleneck anyway, so the difference rarely matters.

Q: If two files have the same hash, how confident can you be they're identical?
A: In practice, extremely confident, though not mathematically certain. A hash maps infinitely many possible inputs to a fixed number of outputs, so collisions must exist. With SHA-256 there are 2²⁵⁶ possible outputs. Even across billions of files, the chance of an accidental collision is astronomically smaller than the chance of a disk error corrupting your data. So "same SHA-256 means same content" is a safe working assumption. The reverse direction is absolute: different hashes always mean different files. With MD5, the same-hash conclusion holds only if nobody could have tampered with the files. If you need certainty, use a matching hash as a signal and then do one final byte-by-byte comparison.

Why the sync tool plans before acting

Concept: The tool runs in two phases. First it scans both sides and builds a complete plan, a list of actions like copy A, update B, delete C. Only then does it execute the plan. It never copies files as it discovers differences.

Why:

Predictability: You know the full scope of changes before anything happens, so a crash halfway through doesn't leave you wondering what was done.
Dry-run / preview: The same plan can be printed instead of executed (--dry-run). That lets you catch mistakes, like "why is it deleting 4,000 files?", before they touch real data.
Testability: Planning is a pure function: given two folder states, it returns a list of actions. You can unit test it with fake data, without touching the filesystem. Only the small executor needs real I/O.
Separation of concerns: Deciding what to do is kept apart from doing it, which makes each part simpler to reason about and change.

Connection forward: The "decide first, then execute recorded steps" idea comes back in Week 11. The Saga pattern breaks a big operation into planned steps with compensating undo actions. The Outbox pattern records intended actions durably before carrying them out. Both rely on the same idea: write down the intended changes first, so they can be inspected, retried, or rolled back.