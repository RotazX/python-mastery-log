from week02.recursion_basics import factorial
from week02.recursive_sum import recursive_sum
from week02.linear_vs_binary import linear_search, binary_search

def test_factorial_normal() -> None:
    assert factorial(5) == 120

def test_factorial_edge() -> None:
    assert factorial(0) == 1

def test_recursive_sum_normal() -> None:
    assert recursive_sum([1, 2, 3 ,4 ,5 ,6]) == 21

def test_recursive_sum_edge() -> None:
    assert recursive_sum([]) == 0

def test_linear_search_normal() -> None:
    assert linear_search([1, 2, 3, 4, 5, 6], 5) == 4

def test_linear_search_edge() -> None:
    assert linear_search([], 5) == None

def test_binary_search_normal() -> None:
    assert binary_search([1, 2, 3, 4, 5, 6], 5) == 4

def test_binary_search_edge() -> None:
    assert binary_search([6, 5, 4, 3, 5,2 ,4], 5) == None
