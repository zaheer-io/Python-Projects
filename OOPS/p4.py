#define class named circle with attributes, and find get area and get perimeter
# import math
#
# class Circle:
#     def __init__(self):
#         self.radius = int(input("Enter the radius: "))
#
#     def perimeter(self):
#         print(f"Perimeter is {float(2 * math.pi * self.radius)}")
#
#     def area(self):
#         print(f"Area is {float(math.pi * (self.radius)**2)}")
#
# r1 = Circle()
#
# r1.perimeter()
# r1.area()


class Bank:
    def __init__(self):
        self.accountno = int(input("Enter the account no: "))
        self.name = input("Enter the account holder name: ")
        self.balance = 0.00

    def showbalance(self):
        print(f"Current balance is : {self.balance}")

    def deposit(self):
        amt = float(input("Enter the amount to deposit: "))
        self.balance += amt

        print("Deposit successful...")
        print(f"New balance is {self.balance}")

    def withdrawn(self):
        amt = float(input("Enter the amount to be withdrawn: "))
        if amt > self.balance:
            print("Empty balance:")
        else:
             self.balance -= amt
             print("Withdrawn successful...")
             print(f"New balance is {self.balance}")


b1 = Bank()
b1.showbalance()
b1.deposit()
b1.withdrawn()
b1.showbalance()

b1.deposit()
b1.withdrawn()

