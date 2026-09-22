
# def factorial(n: int) -> tuple[int | None, str | None]:
#     if n < 0:
#         return None, ValueError("The number should be higher than 0.")
#     if n == 0: # Base case
#         return 1, None
#     elif n == 1: # Base case
#         return 1, None
#     else: # Recursive case
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result, None
    

# def fibonacci(n: int) -> tuple[int | None, str | None]:
#     if n == 0: # Base case
#         return 0, None
#     if n == 1: # Base case
#         return 1, None
#     else: # Recursive case
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#          a, b = b, a + b
#         return b, None

# def main() -> int:
#     try:
#         num = input("Give me a number. ")
#         r_num = int(num)
#     except ValueError:
#         print(f"{num} is not a number.")

#     fac_ans, fac_err = factorial(r_num)
#     if fac_err:
#         print(f"Error = {fac_err}")
#     else:
#         print(f"The factorial of {num} is {fac_ans}.")

#     fib_ans, fib_err = fibonacci(r_num)
#     if fib_err:
#         print(f"Error = {fib_err}")
#     else:
#         print(f"The fibonacci of {num} is {fib_ans}.")

# if __name__ == "__main__":
#     main()

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative.")
    # Base case: 0! is defined as 1, so return directly with no further call.
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!, and each call moves n one step toward 0.
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative.")
    # Base cases: fib(0) = 0 and fib(1) = 1. Two are needed because the
    # recursive case reaches back two steps; with only fib(0), fib(1) would
    # call fib(-1) and never stop.
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case: each number is the sum of the two before it.
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    raw = input("Give me a non-negative integer: ")
    try:
        n = int(raw)
    except ValueError:
        print(f"{raw!r} is not an integer.")
        return

    try:
        fac = factorial(n)
        fib = fibonacci(n)
    except ValueError as err:
        print(f"Error: {err}")
        return

    print(f"factorial({n}) = {fac}")
    print(f"fibonacci({n}) = {fib}")


if __name__ == "__main__":
    main()