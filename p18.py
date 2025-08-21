num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# if num1 > num2 and num1 > num3:
#     print(f"{num1} is greater")
# elif num2 > num3:
#     print(f"{num2} is greater")
# else:
#     print(f"{num3} is greater")

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is bigger")
    else:
        print(f"{num3} is bigger")
else:
    if num2 > num3:
        print(f"{num2} is bigger")
    else:
        print(f"{num3} is bigger")


