
"""
#print 1 to 10 using for loop

for i in range(1, 11):
    print(i)

print("\n\n")
for j in range(1, 12, 2):
    print(j)

print("\n\n")
for i in range(10, 101, 10):
    print(i)

print("\n\n")
for i in range(1, 7):
    print(i ** 2)

print("\n\n")
for i in range(8, -1, -2):
    print(i)

print("\n\n")
for i in range(10, -2, -1):
    print(i)

print("\n\n")
for i in range(-8, 1, 2):
    print(i)

for i  in range(1, 37, i ** 2):
    print(i)

"""


#sum of all numbers in the range 1 to 20

sum = 0

for i in range(1, 21):
    sum += i

print("Sum of numbers (1 to 20) = ", sum)

print("\n")
#given l = [11, 34, 67, 23, 90] sum of numbers greater than 50

l = [11, 34, 67, 23, 90]
sum = 0

for i in l:
    if i > 50:
        sum += i

print("Sum of numbers greater than 50 = ", sum)


d1 = {'num1' : 46, }

print("\n")
#given dictinoary d = {'arun' : 34, 'amal' : 56, 'anu' : 23, 'kiran' : 32} find thae average age

d = {'arun' : 34, 'amal' : 56, 'anu' : 23, 'kiran' : 32}

sum = 0
avg = 0


for i in d.values():
    sum += i

avg = sum / len(d.values())

print("Average age = ", avg)


# print((34 + 56 + 23 + 32) / 4)


print("\n")
#factorial of a number using for loop

n = int(input("Enter a nubmer : "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i

print(f"factorial of {n} is {fact}")


print("\n")
#factors of a number

f = int(input("Enter a number: "))

for i in range(1,f+1):
    if f % i == 0:
        print(i, end=" ")



print("\n")
#multliplication tabel of a number


m = int(input("Enter a number: "))

for i in range(1, 11):
    print(i, " x ", m, " = ", m * i)