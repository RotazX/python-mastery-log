
def generator() -> int:
    return sum(n*n for n in range(1, 1_000_001))

def generator_list() -> int:
    return sum(list(n*n for n in range(1, 1_000_001)))

print(generator())
print(generator_list())

"""
The list comprehension builds all million integers in memory first, 
then hands the finished list to sum. Peak memory holds a million objects, 
and sum can't begin until the last one exists. The generator expression builds nothing. 
It's an object holding a recipe and a position; each time sum asks for the next value, 
it computes one square, hands it over, and forgets it. 
Peak memory is one integer plus the generator's own bookkeeping, 
regardless of whether the limit is a thousand or a billion.
"""
