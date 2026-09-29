
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount 
        self.shortfall = amount - balance

def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    else:
        return balance - amount

if __name__ == "__main__":
    try:   
        print(f"New balance: {withdraw(100, 30)}")
    except InsufficientFundsError as error:
        print(f"The shortfall is {error.shortfall}")

    try:   
        print(withdraw(100, 150))
    except InsufficientFundsError as error:
        print(f"The shortfall is {error.shortfall}")