# #define a fn to check whether a number is perfect no or not
#

def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum

n = int(input("Enter a number: "))

if n == perfect(n):
    print(f"{n} is perfect number")
else:
    print(f"{n} is not perfect")


#define a fn to convert celsius temp to farenheit

# def convert(c):
#     f = (c *9/5) + 32
#     return f
#
# c = float(input("Enter celcius value: "))
# print("Farenheit is ", convert(c))
