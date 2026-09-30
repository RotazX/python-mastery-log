import pytest

def is_prime(n: int) -> bool:
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

@pytest.mark.parametrize("n, expected", [(1, False), (0, False), (89, True), (3, True), (49, False)])

def test_is_prime(n: int, expected: bool) -> None:
    assert is_prime(n) == expected