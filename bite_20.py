""" 
Bite 20. Write a context manager 
"""


class Account:
    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self.balance < 0:
            transactions_list = sorted(self._sorted, reverse = True)
            while sum(transactions_list) < 0:
                transactions_list.pop()
            self._transactions = transactions_list
        
        return self
        

if __name__ == "__main__":
    account = Account()
    with account as acc:
        acc + 10
    print(account.balance)
