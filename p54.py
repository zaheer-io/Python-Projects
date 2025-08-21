"""

def add(a, b):
    s = a + b
    return s

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(add(a, b))

def area_circle(r):
    return 3.14 * (r ** 2)

r = int(input("Enter the radius: "))

print(f"Area of a circle is: {area_circle(r)}")




#defien a function check a number is armstrong or not

def armstrong(n):
    sum = 0

    for i in str(n):
        sum += (int(i) ** len(str(n)))

    if sum == n:
        return True
    else:
        return False



print("Armstrong") if armstrong(n) == True else print("Not an Armstrong")

"""
# n = int(input("Enter a number: "))
#
# print(sum(int(i) ** len(str(n)) for i in str(n)))


def f(*args):
    print(args)

f(10,20)
f(10,20,5,45)

def a(**kwargs):
    print(kwargs)

a(name = 'arum', age = 25)

