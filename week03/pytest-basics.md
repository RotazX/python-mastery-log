## Arrange–Act–Assert
- **Arrange**: set up inputs and state (data, objects, temp files).
- **Act**: call the one thing being tested.
- **Assert**: check the result matches what I expected.
- One behavior per test. If a test needs two Acts, it's probably two tests.

```python
def test_add_note_creates_file(tmp_path):
    # Arrange
    vault = Vault(tmp_path)
    # Act
    vault.add_note("hello", "body text")
    # Assert
    assert (tmp_path / "hello.md").read_text() == "body text"
```

## Why `tmp_path` beats real files
- pytest gives each test a fresh, empty temp folder and cleans it up afterwards.
- A bug in the test can't overwrite or delete my real notes or project files.
- Tests don't depend on what happens to be on my machine, so they run the same way everywhere (my laptop, CI, someone else's computer).
- Tests don't leak state into each other. Leftover files from test A can't make test B pass or fail by accident.

## Cost of NOT having tests (12-week project)
- Every change becomes a gamble. By week 8 I'm editing code I wrote in week 2 and no longer remember why it works.
- Bugs surface late and far from their cause, so debugging takes hours instead of minutes.
- I start avoiding refactors because I'm scared of breaking things. The code rots and each new feature gets slower to add.
- Manual checking ("run it and eyeball it") costs time on every change. Tests pay that cost once.
- **Short version:** no tests is cheap in week 1 and expensive every week after.

## Why write the test before the feature (solo)
- The test forces me to decide what "done" means before I write any code: inputs, outputs, edge cases.
- Writing the call first shows me whether the design is awkward to use. If the test is painful to write, the API is bad.
- Watching it fail first proves the test actually checks something. A test that has never failed might be testing nothing.
- Solo means nobody reviews my code. The tests act as that reviewer, and as notes for future-me.
- **Interview line:** "I don't always do strict TDD, but I often write the test first for the core behavior. It pins down the spec, catches design problems early, and gives me a safety net so I can refactor freely over a long project."