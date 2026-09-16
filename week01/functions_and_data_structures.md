
Parameters are the names you write in the def line — placeholders. Arguments are the actual values you pass when you call it. def is_prime(n: int) -> bool: declares a parameter n; is_prime(17) passes the argument 17. Worth getting straight now because error messages use both words and mean different things by them.

Positional arguments - Matched by order, nothing else. def power(base: int, exp: int) -> int: called as power(2, 3) gives 8; power(3, 2) gives 9. Python has no idea you meant otherwise — position is the only signal. This is why long positional calls like create_user("Bob", 30, True, False) are a maintenance problem: nothing at the call site tells a reader what those booleans mean.

Keyword arguments - Matched by name, order irrelevant. power(exp=3, base=2) is still 8. The point isn't flexibility, it's readability at the call site — create_user(name="Bob", active=True, admin=False) documents itself. Rule to adopt: pass booleans and anything ambiguous by keyword, always.

*args collects leftover positional arguments into a tuple. **kwargs collects leftover keyword arguments into a dict. You've already used the calling side without noticing: print("a", "b", "c") works for any number of arguments because print is defined with *args. You don't need to write these yet. You need to not be confused when you see them in library source or in decorators (Week 5 — every decorator you write will use *args, **kwargs to pass arguments through to the function it wraps).

A pure function does two things: its return value depends only on its arguments, and it changes nothing outside itself. Same input, same output, every time, forever. is_prime(17) is pure.

A side effect is any change outside the function's own return value — writing a file, printing, mutating a list that was passed in, updating a global, hitting a network.

Why this matters, concretely: pure functions are trivial to test (call it, assert the return value), and impure ones aren't (you need a fake filesystem, which is exactly why Week 3 teaches tmp_path). It's also the reason behind your convention of logic functions at the top and printing in the __main__ block — you're deliberately keeping computation pure and pushing side effects to the edges of the program. Tonight's contact book refactor makes this visible: load_contacts() and save_contacts() are unavoidably impure because touching disk is the side effect, while a function that finds a contact in an already-loaded dict can be pure.

Single responisbility means a function should answer to one kind of request.

Before you write any def line again, answer two questions out loud: what exactly comes in, and what exactly goes out. If you can't answer, you don't yet know what the function is for.