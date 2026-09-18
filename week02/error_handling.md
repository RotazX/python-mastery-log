
The exception hierarchy

Every exception in Python is a class, and they form a family tree. At the very top sits BaseException, which also covers things like KeyboardInterrupt (pressing Ctrl+C) and SystemExit (the program closing). You almost never catch those. Just below it is Exception, the parent of all the ordinary errors your code will run into. Under Exception come the specific types: ValueError (right type, wrong value, like int("abc")), TypeError (wrong type entirely, like "5" + 3), KeyError (missing dictionary key), IndexError (list position out of range), FileNotFoundError, ZeroDivisionError, and many more. Some have their own parents too, for example KeyError and IndexError both belong to LookupError.

This matters because except catches the named class and everything beneath it. except ValueError catches only value problems, while except Exception catches nearly everything. The rule is to catch the most specific exception you can, because a broad catch will also swallow bugs you never intended to hide.

EAFP vs LBYL

LBYL, "look before you leap," means checking conditions first and acting only if they are safe: if key in my_dict: value = my_dict[key]. EAFP, "easier to ask forgiveness than permission," means just trying the action and handling the failure if it happens: try: value = my_dict[key] except KeyError: ....

Python generally favors EAFP. It is often cleaner, it avoids checking the same thing twice, and it avoids race conditions where the situation changes between your check and your action (a file can be deleted right after you confirm it exists). LBYL is still fine when the check is cheap and obvious, or when failure is the normal expected case rather than an exception.

When to let an exception propagate instead of catching it

Let an exception travel upward whenever the current function has no good way to fix the problem. Catching an error only makes sense if you can actually do something useful: retry, use a sensible default, ask the user again, or add context and re-raise. If all you would do is print something and carry on with broken data, you are hiding the problem rather than handling it, and the program will fail later in a more confusing place.

A good mental test is to ask, "Does this function know what the right recovery is?" A low-level function that reads a config file usually does not know whether a missing file should stop the program or fall back to defaults, so it should let FileNotFoundError rise. The higher-level code that called it has more context and is the right place to decide. Also let exceptions propagate when they signal a genuine bug, like a TypeError from passing the wrong kind of data, because you want to see that crash and fix the code, not silence it. In short, catch errors where you can handle them meaningfully, and let everything else rise to a level that can.

Crashing vs failing gracefully

A program that crashes on bad input stops completely the moment it meets something it didn't expect. A program that fails gracefully notices the problem, deals with it in a controlled way, and keeps doing as much useful work as it safely can. It also reports clearly what went wrong. Graceful doesn't mean silent. It means the failure is contained, visible, and doesn't take everything else down with it.

The malformed-line example

Imagine a script that reads a data file where every line should look like artist,song,year. Most lines are fine, but line 4,812 says Radiohead,Creep with the year missing. The crashing version looks like this:

python
for line in f:
    artist, song, year = line.strip().split(",")
    save(artist, song, int(year))

When it hits the bad line, the unpacking fails with a ValueError, the whole script dies, and the 4,811 good lines before it may never be saved, along with the thousands after it. The error message also doesn't tell you which line broke.

The graceful version handles that one line and moves on:

python
bad = 0
for n, line in enumerate(f, start=1):
    try:
        artist, song, year = line.strip().split(",")
        save(artist, song, int(year))
    except ValueError:
        bad += 1
        log.warning("Skipped malformed line %d: %r", n, line)
print(f"Done. {bad} bad lines skipped.")

Now one broken line costs you one record, not the entire run. The warning tells you the exact line number and content, so you can fix the source data later. The summary at the end makes sure the problem is noticed instead of quietly buried. Notice that it catches only ValueError, the specific error bad data produces. A real bug elsewhere, like save() failing because the database is down, still crashes loudly, which is what you want.

Why this matters in production

In production, input comes from the real world, and real-world data is messy: files get edited by hand, feeds change format, websites return junk. At scale, some bad input is basically guaranteed. If a single malformed line can kill the whole job, your program becomes only as reliable as the worst line it will ever see, and that's not very reliable. Jobs that run automatically at night are the worst case, because nobody is watching when they die, and you find out hours later that nothing was processed.

Graceful failure keeps the damage proportional to the problem. It also protects you from half-finished states, where a crash midway leaves some data written and some not. And the logging gives you a trail to diagnose issues afterwards instead of guessing.

The balance to keep in mind ties back to the propagation question from before. Handle the errors you expect and understand, like a malformed line in data you don't control, and let unexpected ones crash, because those usually mean a bug in your own code. There's also a limit: if 90% of lines are malformed, that's not bad data anymore, it's probably the wrong file or a changed format, and the program should stop and say so rather than cheerfully skip almost everything.