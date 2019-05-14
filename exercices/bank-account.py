class Account():

    def __init__(self, owner, balance = 0):
        self.balance = balance
        self.owner = owner

    def deposit(self, value):
        self.balance += value
        print(f'\nDeposit of ${value} accepted!')

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            print(f'\nWithdrawal of ${value} accepted!')
        else:
            print(f'\nWithdrawal of ${value} rejected! Your funds are unavailable.')

    def __str__(self):
        return f'Account Owner:   {self.owner}\nAccount Balance: ${self.balance}'

account1 = Account('Caio', 100)

# print(account1.owner)
# print(account1.balance)
print(account1)

account1.deposit(50)
print(f'Current Balance: ${account1.balance}')

deposit = account1.deposit(150)
print(f'Current Balance: ${account1.balance}')

withdraw = account1.withdraw(200)
print(f'Current Balance: ${account1.balance}')

withdraw = account1.withdraw(100)
print(f'Current Balance: ${account1.balance}')

deposit = account1.deposit(200)
print(f'Current Balance: ${account1.balance}')

withdraw = account1.withdraw(300)
print(f'Current Balance: ${account1.balance}')
