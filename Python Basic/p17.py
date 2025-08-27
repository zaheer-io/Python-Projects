#wap to check a number is 3 digit no or not
"""

num1 = int(input("Enter a number: "))

num1str = str(num1)

if len(num1str) == 3:
    print(num1,"is a 3 digit no")
else:
    print(num1, "is not a 3 digit no")

#wap to check whether the last digit is a multiple of 3 or not
print("\n\n")
num2 = int(input("Enter a number: "))

num2int = num2 % 10
if num2int % 3 == 0:
    print(f"{num2} last digit ({num2int}) is a multiple of 3")
else:
    print(f"{num2} last digit ({num2int})is not a multiple of 3")

#wap to check whether an entered character is vowel or not
print("\n\n")
str3 = input("Enter a letter: ")
vowel = "aeiouAEIOU"

if str3 in vowel:
    print(f"{str3} is a vowel")
else:
    print(f"{str3} is not a vowel")

#wap to check whether an entered no is present in the given list or not
print("\n\n")

l = [23,56,12,80]

num4 = int(input("Enter a number: "))

if num4 in l:
    print(f"{num4} present in the list")
else:
    print(f"{num4} present not in the list")

#wap to check whether an entered name is present in dictionary or not
print("\n\n")


d = {'name' : 'arun', 'age' : 25, 'place' : 'ekm'}

str5 = input("Enter a name: ")

if str5 in d['name']:
    print(str5, "present")
else:
    print(str5, "not present")


#wap to check two entered strings are equal or not
print("\n\n")


str6 = input("Enter first name: ")
str7 = input("Enter second name: ")

if str6 == str7:
    print("same")
else:
    print("not same")

#wap to check whether the given string is palindrome or not
print("\n\n")

str8 = input("Enter string: ")

if str8[::-1] == str8:
    print(f"{str8}Palindrome")
else:
    print(f"{str8}not palindrome")
"""
#wap to check find the maximum of two numbers
print("\n\n")

num8 = int(input("Enter first number: "))
num9 = int(input("Enter second number: "))

if num8 > num9:
    print(f"{num8} is bigger")
else:
    print(f"{num9} is bigger")

