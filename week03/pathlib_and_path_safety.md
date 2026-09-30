
## Why `Path.resolve()` matters
- `resolve()` turns a path into its real, absolute form: it collapses `..`, follows symlinks, and removes tricks.
- Without it, `base / "../../../etc/passwd"` *looks* like it's inside `base` but actually points outside it.
- Safe pattern: resolve first, then check the result is still inside the allowed folder.

```python
from pathlib import Path

def safe_join(base: Path, user_name: str) -> Path:
    base = base.resolve()
    target = (base / user_name).resolve()
    if not target.is_relative_to(base):   # Python 3.9+
        raise ValueError(f"Path escapes base folder: {user_name}")
    return target
```

- Check *after* resolving. Checking the raw string for `..` misses symlinks and encoded tricks.

## `os.path` vs `pathlib`
- `os.path`: older, works on plain strings with functions: `os.path.join(a, b)`, `os.path.exists(p)`.
- `pathlib`: paths are objects with methods: `base / "notes" / "a.md"`, `p.exists()`, `p.read_text()`.
- Same power underneath; `pathlib` is just cleaner and harder to misuse.

## Why this curriculum defaults to `pathlib`
- More readable: `/` for joining beats nested `os.path.join` calls.
- Everything lives in one place (`.suffix`, `.stem`, `.parent`, `.glob()`, `.read_text()`) instead of spread across `os`, `os.path`, `glob`, `shutil`.
- Works the same on Windows and Mac/Linux, so there are no manual `\` vs `/` headaches.
- Safety helpers like `resolve()` and `is_relative_to()` are built in, which makes the OpenSSF check easy.
- It's the modern standard; most current libraries accept `Path` objects.

## What goes wrong without the containment check (sync tool)
- **Scenario:** my tool syncs files from a source folder into `~/Backups/vault/`. It builds the destination as `dest / relative_path` for each file.
- A file in the source (malicious, or just a weird symlink or bad filename) has the relative path `../../.ssh/authorized_keys` or `../../.bashrc`.
- Without resolve-and-check, the tool happily writes to `~/.ssh/authorized_keys` or `~/.bashrc`, *outside* the backup folder.
- **Result:** my real config gets overwritten silently. Worst case, an attacker's SSH key gets installed and they can log into my machine. Mild case, I lose settings and never know why.
- A sync tool is especially risky because it writes *and* often deletes. A "delete files not in source" step pointed outside the folder could wipe real data.
- **Fix:** resolve every destination path and refuse (raise or skip and log) anything not inside `dest.resolve()`. Treat every filename from outside as untrusted input.