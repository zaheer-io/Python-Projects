#p4
from functools import reduce
from traceback import print_tb

# num1 =  int(input("Enter a number: "))
# num2 = int(input('Enter second number: '))
#
# print(f'Sum is {num1 + num2}')
# print(f'Difference is {num1 - num2}')
# print(f'Product is {num1 * num2}')
# print(f'Quotient is {num1 / num2}')

# num1 = int(input('Enter a number: '))
# print(num1 ** 3)


# num = int(input("Enter a number: "))
#
# if num % 2 == 0:
#     print(f'{num} is Even number')
# else:
#     print(f'{num} is odd number')

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
#
# if num1 > num2:
#     print(f'{num1} is larger')
# else:
#     print(f'{num2} is larger')


# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# num3 = int(input('Enter third number: '))
#
# if num1 > num2:
#     if num1 > num3:
#         print(f'{num1} is bigger')
#     else:
#         print(f'{num3} is bigger')
# else:
#     if num2 > num3:
#         print(f'{num2} is bigger')
#     else:
#         print(f'{num3} is bigger')


# num = int(input('Enter number: '))
#
# if num > 0:
#     if num % 2 == 0:
#         print(f'{num} is Positive even number')
#     else:
#         print(f'{num} is Positive odd number')
# elif num < 0:
#     if num % 2 == 0:
#         print(f'{num} is Negative even number')
#     else:
#         print(f'{num} is Negative odd number')
# elif num == 0:
#     print(f'{num} is zero')


# num = int(input('Enter number: '))
# prime = True
#
# for i in range(2, num):
#     if num % i == 0:
#         prime = False
#         break
#
# print(f'{num} is not prime') if not prime or num < 2 else print(f'{num} is prime')


# num = int(input('Enter number: '))
# factors = []
#
# for i in range(1, num+1):
#     if num % i == 0:
#         factors.append(i)
#
# print(factors)

# num = int(input('Enter number: '))

#string method

# strNum = str(num)
#
# revNum = (strNum[::-1])
# print(revNum)

#using arithmetic method

# rev = 0
#
# while num != 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
#
# print(rev)

# nSum = 0
# for i in range(1, 11):
#     nSum += i
#
# print(f'Sum of 1 to 10 is {nSum}')
#
# sSquare = 0
# for i in range(1, 11):
#     sSquare += i ** 2
#
# print(f'Sum of squares of 1 to 10 is {sSquare}')

# nPro = 1
# for i in range(1, 11):
#     nPro *= i
#
# print(f'Sum of product of 1 to 10 is {nPro}')


# string = input("Enter a string : ")
#
# vowels = 'aeiou'
# countVowels = 0
# countSpace = 0
# countNum = 0
# countConsonants = 0
#
# for c in string.lower():
#     if c in vowels:
#         countVowels += 1
#     if c == ' ':
#         countSpace += 1
#     if c.isnumeric():
#         countNum += 1
#     if c.isalpha() and c not in vowels:
#         countConsonants += 1
#
#
# print(f'count of vowels {countVowels}')
# print(f'count of spaces {countSpace}')
# print(f'count of Numbers {countNum}')
# print(f'count of consonants {countConsonants}')

# num = int(input('Enter number: '))

# fact = 1
# for i in range(1, num+1):
#     fact *= i
#
# print(fact)


# def find_fact(num):
#     if num < 0:
#         raise ValueError('Negative number')
#     if num <= 1:
#         return 1
#     return num * find_fact(num - 1)
#
# print(find_fact(num))

# l = [12,75,67,13,56,11]
#
# evenList = []
# oddList = []
# lList = []
#
# for i in l:
#     if i < 50:
#         lList.append(i)
#     if i % 2 == 0:
#         evenList.append(i)
#     if i % 2 == 1:
#         oddList.append(i)
#
# print(evenList, oddList, lList)
#
# l = [1,1,2,3,4,5,6,6,7,7]
# newList = []
#
# for i in l:
#     if i not in newList:
#         newList.append(i)
#
# print(newList)

# fruits = ['apple','banana','orange','pineapple','avocado']
# newList = []
#
# for i in fruits:
#     if len(i) > 5:
#         newList.append(i)
#
# print(newList)


# students = {
#   'Asha':[98,82,91,97,89],
#   'John':[88,76,92,85,77],
#   'Maya':[70,70,84,79,88]
# }
#
# def find_grade(mark):
#     if mark > 80:
#         return 'A'
#     elif mark > 60:
#         return 'B'
#     elif mark > 40:
#         return 'C'
#     elif mark > 20:
#         return 'D'
#     else:
#         return 'E'
#
# stdDetails = {}
#
# for name, mark in students.items():
#     avg = sum(mark) / len(mark)
#     # stdDetails.setdefault(name, {
#     #     'avg' : avg,
#     #     'mark' : find_grade(avg)
#     # })
#
#     stdDetails.update({name : {
#         'avg' : avg,
#         'mark' : find_grade(avg)
#     }})
#
# print(stdDetails)


# l = [1,2,3,4]
#
# sqr = list(map(lambda x : x ** 3, l))
# print(sqr)
#
# from math import sqrt as sq
#
# sqrts = list(map(lambda x : sq(x), l))
# print(sqrts)

# l = [25,16,89,84,54,12,4,36,17,83]
#
# print(list(filter(lambda x : x % 2 == 0, l)))
# print(list(filter(lambda x : x % 3 == 0, l)))
# print(list(filter(lambda x : x > 50, l)))

# l = [12,-4,78,-34,90,45,16,26,-2,-11,-3]
#
# print(reduce(lambda x, y : x + y, list(filter(lambda x : x > 0 and x % 2 == 0, l))))
#
# print(reduce(lambda x, y : x + y, list(filter(lambda x : x < 0 and x % 2 == 1, l))))


# inp = int(input('Enter the length: '))
# arr = []
#
# for i in range(0, inp):
#     arr.append(int(input(f'Enter {i+1} value: ')))
#
# print(arr)
#
# for i in arr:
#     for j in arr:
#         if i > j:
#             arr[i], arr[j] = arr[j], arr[i]
#
# print(arr)