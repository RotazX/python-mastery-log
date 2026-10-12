
def factorial(n: int) -> int:
    if n < 0:
        raise(ValueError())

    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * factorial(n-1)


def fibonacci(n: int) -> int:
    if n < 0:
        raise(ValueError())
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    num = int(input("Write a number: "))
    try:
        print(factorial(num))
    except ValueError:
        print("Wrong num")

    try:
        print(fibonacci(num))
    except ValueError:
        print("Wrong num")