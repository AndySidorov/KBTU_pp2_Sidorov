class Account():
    def __init__(self, name, money):
        self.owner = name
        self.balance = int(money)
    def deposit(self):
        self.balance += int(input())
    def withdraw(self, m):
        if m <= self.balance:
            self.balance -= m
        else:
            print("Insufficient funds to pay")
    def show(self):
        print(self.balance)
name = input()
balance = int(input())
guy = Account(name, balance)
guy.deposit()
guy.show()
guy.withdraw(int(input()))
guy.show()