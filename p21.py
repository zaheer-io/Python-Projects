#wap to check whether a number is positive even or positive odd and negative odd or negative even

num1 = int(input("Enter a number: "))

if num1 > 0:
    if num1 % 2 == 0:
            print("Positive even")
    else:
            print("Positive odd")
elif num1 < 0:
    if num1 % 2 == 0:
            print("negative even")
    else:
            print("negative odd")
else:
    print("you entered zero")