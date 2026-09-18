
"""Defining and raising a custom exception."""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""

    def __init__(self, balance: float, amount: float) -> None:
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        super().__init__(
            f"cannot withdraw {amount:.2f} from a balance of {balance:.2f}"
        )


def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


def main() -> None:
    balance = 100.0

    for amount in (30.0, 500.0, -5.0):
        try:
            balance = withdraw(balance, amount)
        except InsufficientFundsError as err:
            print(f"declined: short by {err.shortfall:.2f}")
        except ValueError as err:
            print(f"bad request: {err}")
        else:
            print(f"withdrew {amount:.2f}, balance now {balance:.2f}")


if __name__ == "__main__":
    main()