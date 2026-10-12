
def is_valid(s: str) -> bool:
    pairs, stack = {"(": ")", "[": "]", "{": "}"}, []
    for ch in s:
        if ch in pairs:
            stack.append(pairs[ch])
        elif not stack or stack.pop() != ch:
            return False
    return not stack

if __name__ == "__main__":
    for s, want in [("", True), ("()[]{}", True), ("{[()]}", True), ("(())()", True),
                    ("(]", False), ("([)]", False), ("(((", False), (")", False), (")(", False)]:
        assert is_valid(s) == want, s
    print("all tests passed")
