def add(a, b):
    return a + b

print(add(10,20))


print((lambda a, b: a + b )(10,20))

#factorial of a number

n = int(input("Enter a number: "))

fact = lambda x: 1 if x == 0 else x * fact(x - 1)

print(fact(n))

