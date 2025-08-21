#write a program to find simple interest

p = int(input("Enter principle amount: "))
n = int(input("Enter year: "))
r = int(input("Enter Rate of interest: "))

interest = (p * n * r) / 100

print("Simple interest is ",interest)
