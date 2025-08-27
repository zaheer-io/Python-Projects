num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 > num2 and num1 > num3 and num1  > num4:
    print(f"{num1} is bigger")
elif num2 > num3 and num2 > num4:
    print(f"{num2} is bigger")
elif num3 > num4:
    print(f"{num3} is bigger")
else:
    print(f"{num4} is bigger")