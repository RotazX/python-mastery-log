
class InsufficientFundsError(Exception):
    def __init__(self, balance: float, amount: float) -> None:
        self.balance = balance
        self.amount = amount 
        self.shortfall = amount - balance
        super().__init__(f"Insufficient funds: short by {self.shortfall}")

def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

if __name__ == "__main__":
    for balance, amount in [(100, 30), (100, 150)]:
        try:
            print(f"New balance: {withdraw(balance, amount)}")
        except InsufficientFundsError as error:
            print(f"The shortfall is {error.shortfall}")