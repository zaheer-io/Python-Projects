
"""
n = 1234

s = str(n)

for i in s:
    print(i, end=" ")

#sum of digits in a number

# n = int(input("Enter a number: "))
print()

sum = 0

for i in s:
    sum +=int(i)

print(sum)

#check whether a given number is an amstorng

n = int(input("Enter a number: "))

s = str(n)
power = len(str(n))
sum = 0

for i in s:
    sum += (int(i) ** power)

if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

"""

#Revese of a number

n = 1234
rev = ""

for i in str(n):
    rev = i + rev

print(rev)

n = 1234
rev1 = 0
p = 0

while n > 0:
    p = n % 10
    rev1 = (rev1 * 10) + p
    n = n // 10

print(rev1)

s = "hello world"
rev = ""

for i in s:
    rev = i + rev



print(rev)