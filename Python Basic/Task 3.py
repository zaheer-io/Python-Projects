"""

# # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
# from http.cookiejar import cut_port_re

for i in range(1, 101, 1):
    if i % 2 == 0 and i % 5 == 0:
        print(i, end=", ")

print("\n")

# # 2.Take a string input from the user and print the reverse using a for loop.(without [::-1])

e = input("Enter the string: ")
r = ""

for i in e:
    r = i + r

print(r)

print("\n")
# #3.Given a number n, write a program that uses a for loop to compute the sum of its digits.
# # Example: n = 1234 → Output: 10

n = int(input("Enter a number: "))
e = str(n)
s = 0

for i in e:
    s = s + int(i)

print(f"Sum of digits of {n} is {s}")

print("\n")



# # 4.Print the cumulative sum of a list.
# # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]

l = int(input("Enter the limit of the list: "))
culist = []

for i in range(1, l + 1, 1):
    culist.append(int(input(f"Enter the {i} th digit: ")))

sum = 0
sumlist = []

for i in culist:
    sum += i
    sumlist.append(sum)

print(culist)
print(sumlist)



print("\n")
# # 5.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25

a = int(input("Enter first number: "))
b = int(input("Enter the last number: "))
sum = 0

for i in range(a, b + 1):
    sum += i

print(f"Sum of numbers in between {a} and {b} is {sum}")


print("\n")
# 6.Given a list, sum only the elements at even indices.
# Example:
#  → Sum = 10 + 30 + 50 = 90
l=[10, 20, 30, 40, 50]

sumlist = 0

for index, value in enumerate(l):
    sumlist += value if index % 2 == 0 else 0


print(sumlist)




print("\n")
#7.Given a list, sum the elements until a 0 is encountered (stop at 0).
# Example: [1, 3, 5, 0, 8, 10] → Output: 9
l=[1, 3, 5, 0, 8, 10]
sum = 0

for i in l:
    if i == 0:
        print(sum)
        break
    else:
        sum += i


print("\n")
# 8.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.


for i in range(1, 1001):
    if i % 7 == 0:
        print(f"No found {i}")
        break



print("\n")
# 9.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.
l=['orange','apple','banana','kiwi']

for i in l:
    if len(i) >= 5:
        print(i)
    else:
        continue


print("\n")
# 10. Loop from 1 to 30 and print all numbers except those divisible by 4. Use continue.

for i in range(1, 31):
    if i % 4 == 0:
        continue
    else:
        print(i, end=" ")



print("\n")
# 11.From a list of numbers, create a new list containing the squares of each element.
# Input: [1, 2, 3] → Output: [1, 4, 9]

l = [1, 2, 3, 4, 5, 6]
sl = []

for i in l:
    sl.append(i ** 2)

print(sl)



print("\n")
# 12Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"
s="hello world"
vow = ['a', 'e','i', 'o', 'u']
for i in s:
    if i in vow:
        continue
    print(i, end="")


"""
print("\n")
#
# 13.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).




# 14.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"

word = "abc123x7z"



# 15.Given a list of strings, create a new list containing the length of each string.
# Input: ["cat", "banana", ""] → Output: [3, 6, 0]
# 16.Given a list of words, create a string made of the first letter of each word.
# Input: ["Python", "Is", "Great"] → Output: "PIG"
# 17.From a list of numbers, create a list where each element is the cumulative product so far.
# Input: [2, 3, 4] → Output: [2, 6, 24]

# 18.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
# Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0]

# 19.print the pattern
# 1
# 4 9
# 16 25 36
#
#
# 20.print the pattern
#    **
#   ****
#  ******
# ********


list = [['india', 'america', 'caneda'], ['china', 'bhuttan', 'malesia']]

print(list)

for i in list:
    print(i)


for i in list:
    for j in i:
        print(j)





d = {1 : ['dog', 'cat', 'sheep'], 2 : ['tiger', 'lion', 'bear']}

for i in d.values():
    for j in i:
        print(j, end=" ")

print()

l = ['apple', 'orange', 'pineapple']

for i in l:
    for j in i:
        print(j, end=" ")
    print()