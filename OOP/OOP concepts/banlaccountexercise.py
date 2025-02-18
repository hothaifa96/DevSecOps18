import datetime


class Bank:
    def __init__(self):
        self.__accounts = {}

    def create_account(self, account):
        self.__accounts[account.id] = account

    def find_account(self, acc_id):
        return self.__accounts.get(acc_id)


class BankAccount(Bank):
    def __init__(self, customer, balance, id):
        super().__init__()
        self.customer = customer
        self.balance = balance
        self.id = id
        self._transactions = []

    def withdraw(self, amount):
        if self.balance - amount > 0:
            print('successfully withdrew')
            self.balance -= amount
            self._transactions.append(f'{self.customer} withdrew {amount}')
            return amount

    def deposit(self, amount):
        amount = abs(amount)
        self._transactions.append(f'{self.customer} deposit {amount}')
        self.balance += amount

    def show_transactions(self):
        print(f'transactions for {self.customer}')
        for transaction in self._transactions:
            print(transaction)

    def __str__(self):
        greet = 'good morning' if 0<datetime.datetime.now().hour <12 else 'good evening'
        return greet +f' {self.customer} your balance:{self.balance}₪' \
               f' in {self.id} account'


class CheckingAccount(BankAccount):
    def __init__(self, customer, balance, id, overdraft=0):
        super().__init__(customer, balance, id)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount < self.balance + self.overdraft:
            self.balance -= amount
            self._transactions.append(f'{self.customer} withdrew {amount}')
            print(f'the balance updated balance {self.balance}')


class LoanAccount(BankAccount):
    def __init__(self, customer, balance, id):
        super().__init__(customer, -balance, id)  # negative balance
        self.debt = balance

    def pay_loan(self, amount):
        self.balance += amount
        self.debt -= amount


class SavingAccount(BankAccount):
    def __init__(self, customer, balance, id, interest_rate: float = 0.02):
        super().__init__(customer, balance, id)  # negative balance
        self.interest_rate = interest_rate
        self.interest = 0.0

    def add_interest(self):
        self.interest = self.balance * self.interest_rate
        print(f'the interest for now is {self.interest}')


def generate_email(name):
    return name + '@gmail.com'


bank_name = 'DevOps Bank LTD'

if __name__ == '__main__':
    print('hello')
