#p4

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