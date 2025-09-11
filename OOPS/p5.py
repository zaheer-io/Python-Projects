import random
from random import randint

acccounts = []

class Bank:

    def __init__(self, name):
        self.accname = name
        self.accountno = random.randint(1000, 9999)
        self.balance = 0.00

        print("Account successfully created ")
        print(f"Account holder name {self.accname}")
        print(f"Account number {self.accountno}")
        print(f"Account balance {self.balance}")

    def depost(self, amount):
        self.balance += amount
        print(f"New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance ")
        else:
            self.balance -= amount
            print(f"New balance is {self.balance}")

    def findbalance(self):
        print(f"Balance is {self.balance}")


def findaccount(accno):
    for i in acccounts:
        if i.accountno == accno:
            return i
        else:
            return None


while True:
    print("\n===== Bank Menu =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            name = input("Enter your name: ")
            acc = Bank(name)
            acccounts.append(acc)

        case 2:
            accno = int(input("Enter your account number: "))
            if findaccount(accno):
                amount = int(input("Enter amount to deposit: "))
                acc.depost(amount)
            else:
                print("Account not found")

        case 3:
            accno = int(input("Enter the account number: "))

            if findaccount(accno):
                amount = int(input("Enter amount to be withdraw: "))
                acc.withdraw(amount)
            else:
                print("Account not found")

        case 4:
            accno = int(input("Enter account no: "))
            if findaccount(accno):
                acc.findbalance()
            else:
                print("Account not found")

        case 5:
            exit()
        case 6:
            for i in acccounts:
                print(i.accname, i.balance)
