import random

accounts = []

class Bank:
    def __init__(self, name):
        self.name = name
        self.accno = random.randint(1000, 9999)
        self.balance = 0.0
        print(f"\n Account created successfully!")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.accno}")
        print(f"Initial Balance: {self.balance}\n")

    def deposit(self, amount):
        self.balance += amount
        print(f" Deposit successful! New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(" Insufficient balance!")
        else:
            self.balance -= amount
            print(f" Withdraw successful! New balance: {self.balance}")

    def show_balance(self):
        print(f"Account {self.accno} Balance: {self.balance}")


def find_account(accno):
    for i in accounts:
        if i.accno == accno:
            return i
    return None


# Menu driven loop
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
            name = input("Enter account holder name: ")
            acc = Bank(name)
            accounts.append(acc)

        case 2:
            accno = int(input("Enter account number: "))
            acc = find_account(accno)
            if acc:
                amt = float(input("Enter amount to deposit: "))
                acc.deposit(amt)
            else:
                print("Account not found!")

        case 3:
            accno = int(input("Enter account number: "))
            acc = find_account(accno)
            if acc:
                amt = float(input("Enter amount to withdraw: "))
                acc.withdraw(amt)
            else:
                print("Account not found!")

        case 4:
            accno = int(input("Enter account number: "))
            acc = find_account(accno)
            if acc:
                acc.show_balance()
            else:
                print("Account not found!")

        case 5:
            print("Thank you for using the bank system!")
            break

        case _:
            print("Invalid choice, try again!")
