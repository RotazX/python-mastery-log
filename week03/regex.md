
Core regex syntax
.: any single character (except newline)
*: previous item 0 or more times
+: previous item 1 or more times
?: previous item 0 or 1 times (optional)
[]: character set, one of these chars ([a-z], [0-9])
(): group, capture or apply quantifiers to a chunk
\d: digit
\w: word character (letter, digit, _)
^: start of string/line
$: end of string/line

Why "mostly works" regex is dangerous

A regex that works on your test cases gives false confidence, so nobody adds other checks. In security or file handling, the edge cases are where the damage happens. A path filter .*\.txt also matches evil.txt.exe, and a validator without ^...$ anchors accepts input that only contains a valid part. With no regex, you know the input is unchecked and you're careful. A "mostly works" regex hides the gap.

Why sync tools need exclusion patterns
Without exclusions, the tool mirrors everything: junk, caches, secrets, and repo internals.
.git/: syncing it between machines can corrupt the repo, because two copies of git's internal state overwrite each other mid-operation. Git should handle versioning, not the sync tool.
Temp files (*.tmp, ~$doc.docx, .DS_Store, __pycache__/, node_modules/): thousands of useless files get transferred. Partial or locked files can cause errors or conflicts.
Secrets (.env): these can end up copied somewhere less secure.
Exclusions are usually glob or regex patterns, so the regex rule above applies: a sloppy pattern can silently skip files you need or include files you meant to block.