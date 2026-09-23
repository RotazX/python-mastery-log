from custom_exceptions import InsufficientFundsError

class BankAccount:
    def __init__(self, balance: float = 0.0) -> None:
         self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
             raise ValueError(f"amount must be positive, got {amount}")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
                raise ValueError(f"amount must be positive, got {amount}")
        if amount > self._balance:
                raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        
    def get_balance(self) -> float:
        return self._balance

if __name__ == "__main__":
    account = BankAccount(100.0)

    account.deposit(50.0)
    print(f"After deposit: {account.get_balance()}")

    account.withdraw(30.0)
    print(f"After withdrawal: {account.get_balance()}")

    try:
        account.withdraw(500.0)
    except InsufficientFundsError as e:
        print(f"Withdrawal refused: {e}")
    print(f"Balance unchanged: {account.get_balance()}")

    try:
        account.deposit(-10.0)
    except ValueError as e:
        print(f"Deposit refused: {e}")