# num = int(input('Enter a number: '))
# temp = num
# p = len(str(num))
# arm = 0
#
# while num != 0:
#     d = num % 10
#     arm += d ** p
#     num //= 10
#
# print(f'{temp} is armstrong') if temp == arm else print(f'{temp} is not armstrong')
from itertools import count
from math import sqrt

# primeList = []
# isPrime = True
#
# for i in range(2, 51):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         primeList.append(i)
#
# print(primeList)

# string = input('Enter a word : ')

# freq = {}
# count = 0
#
# for c in string:
#     for i in range(0, len(string)):
#         if c == string[i]:
#             count += 1
#     freq[c] = count
#     count = 0
#
# print(freq)

# freq = {}
#
# for ch in string:
#     if ch in freq.keys():
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
#
# print(freq)


# length = int(input('Enter the length of the list: '))
# l = []
#
# for i in range(0, length):
#     l.append(int(input(f'Enter {i+1} value: ')))
#
# lar = 0 # 3 2 5 6 9 8
# secLar = 0
#
# for i in l:
#     if i > lar:
#         secLar = lar
#         lar = i
#
# print(lar)
# print(secLar)


# length = int(input('Enter the length of the list: '))
# l = []
#
# for i in range(0, length):
#     l.append(int(input(f'Enter {i+1} value: ')))
#
# newList = []
#
# for i in l:
#     if i not in newList:
#         newList.append(i)
#
# print(newList)


# string = input('Enter the string: ')
#
# newStr = string.replace(' ', '').upper()
#
# print('Palindrome') if newStr == newStr[::-1] else print('Not palindrome')



# length = int(input('Enter the length of the tuple: '))
# temp = []
#
# for i in range(length):
#     temp.append(int(input(f'Enter {i+1} value: ')))
#
# t = tuple(temp)
#

# newDict = {number : number ** 3 for number in range(1, 11)}
# print(newDict)

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} FizzBuzz')
#     elif i % 3 == 0:
#         print(f'{i} Fizz')
#     elif i % 5 == 0:
#         print(f'{i} Buzz')

# n = int(input('Enter the number: '))
#
# for i in range(1, n):
#     print(' ' * (n - i), '*' * ((i * 2) -1))

# n = int(input("Enter the number: "))
#
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '*' * ((2 * i) - 1))

# n = int(input('Enter the number: '))

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(' ', end='')
#     print('*' * (2*i - 1))


# n = int(input('Enter the number: '))
# k = 1
#
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(k, end='  ')
#         k+=1
#     print()
#



# for i in range(1, 6):
#     for j in range(1, 6-i+1):
#         print(' ', end='')
#     print('*' * ((2 * i) - 1))



# string = input('Enter a sentence: ')

# words = string.split()
# wordsCount = {}
#
# for i in words:
#     if i in wordsCount.keys():
#         wordsCount[i] += 1
#     else:
#         wordsCount[i] = 1
#
# print(words)
# print(wordsCount)


# i don't get first start fom z to r, z, a, h, e the e apprar stop and final is zahe -> 4 lenght next whyt start with 2nd position ? if strt a, h , e then e apprar final is ahe ???

# string = input('Enter a string : ')
#
# stbDict = {}
#
# def findSubstring(n, s):
#     seen = ""
#     for i in range(n, len(s)):
#         if s[i] not in seen:
#             seen += s[i]
#         elif s[i] in seen:
#             stbDict[seen] = len(seen)
#             seen = ""
#     return stbDict
#
#
# for i in range(0, len(string)):
#     findSubstring(i, string)
#
# print(stbDict)
# print(max(stbDict.items()))

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
#
#
# while True:
#     print('_________Menu________')
#     print('1. Addition')
#     print('2. Substraction')
#     print('3. Multiplication')
#     print('4. Division')
#     print('5. Remainder')
#     print('6. Exit')
#
#     choice = int(input('Enter the choice: '))
#
#     match(choice):
#         case 1:
#             print(f'sum of {num1} and {num2} is {num1 + num2}')
#
#         case 2:
#             print(f'sub of {num1} and {num2} is {num1 - num2}')
#
#         case 3:
#             print(f'Product of {num1} and {num2} is {num1 * num2}')
#
#         case 4:
#             print(f'Division of {num1} and {num2} is {num1 / num2}') if num2 != 0 else print('Not divisible by zero')
#
#         case 5:
#             print(f'Remainder of {num1} and {num2} is {num1 % num2}')
#
#         case 6:
#             break
#
#         case _:
#             print('Enter valid input')


# import os
#
#
# fName = input('Enter file name: ')
#
# def check_file(f):
#     return os.path.exists(f)
#
# while True:
#     print()
#     print('1. Create file: ')
#     print('2. Read file')
#     print('3. Append file')
#     print('4. Search File')
#     print('5. Delete file')
#     print('6. Exit')
#
#     choice = int(input('\nEnter your choice: '))
#
#     match choice:
#         case 1:
#             if check_file(fName):
#                 qus = input("File already exist, do you want to rewrite it ? 'y' for yes and 'n' for no").upper()
#                 if qus == 'Y':
#                     with open(fName, 'w') as file:
#                         file.write(input('Enter the Content to write: ') + '\n')
#                         print('Content writed sucessfully')
#                 else:
#                     continue
#             else:
#                 with open(fName, 'w') as file:
#                     file.write(input('Enter the Content to write: ') + '\n')
#                     print('Content writed sucessfully')
#
#         case 2:
#             if not check_file(fName):
#                 print('File not found')
#             else:
#                 with open(fName, 'r') as file:
#                     print(file.read())
#
#         case 3:
#             if not check_file(fName):
#                 print('File not found')
#             else:
#                 with open(fName, 'a') as file:
#                     file.write(input('Enter the content: ') + '\n')
#                     print('Content writed successfully')
#
#         case 4:
#             if not check_file(fName):
#                 print('File not found')
#             else:
#                 with open(fName, 'r') as file:
#                     print('word found') if input('Enter the string: ') in file.read() else print('word not found')
#
#         case 5:
#             if not check_file(fName):
#                 print('file not found')
#             else:
#                 if os.remove(fName):
#                     print('File Deleted Successfully')
#                 else:
#                     print('Failed')

# vowels = 'aeiou'
# vowelsCount = 0
# wordsCount = 0
# longestWords = []
# longWord = ''
#
#
#
# with open('sample.txt', 'r') as file:
#     content = file.read()
#     for i in content.lower():
#         if i in vowels:
#             vowelsCount += 1
#
#     for i in content.split():  #hai hello what's your goodName hi
#         if len(i) > len(longWord):
#             longestWords.clear()
#             longestWords.append(i)
#             longWord = i
#         elif len(i) == len(longWord):
#             longestWords.append(i)
#
#
#
#
#     print(f'Longest word {longestWords}')
#     print(f'Vowels count {vowelsCount}')
#     print(f'Words count {len(content.split())}')
#
# oldWord = input('Old word: ')
# newWord = input('New word: ')
#
# with open('sample.txt', 'r') as file:
#     content = file.read()
#     print(content)
#
# if oldWord in content:
#     newContent = content.replace(oldWord, newWord)
#
#     with open('sample.txt' , 'w') as file:
#         file.write(newContent)
#
#     print('Replace word successfully')
#
#     with open('sample.txt', 'r') as file:
#         print(file.read())
#
#
#
# else:
#     print('word not found')

print("Password Validator")
print("Minimum 8 chars, At least 1 uppercase, 1 lowercase, 1 digit, 1 special char")

password = input("\nEnter the password: ")

# Initialize conditions
validator = {
    'upper': False,
    'lower': False,
    'digit': False,
    'special': False,
    'space': False
}

# Check each character
for ch in password:
    if ch.isupper():
        validator['upper'] = True
    elif ch.islower():
        validator['lower'] = True
    elif ch.isdigit():
        validator['digit'] = True
    elif not ch.isalnum() and not ch.isspace():
        validator['special'] = True
    elif ch.isspace():
        validator['space'] = True

# Check minimum length
length_valid = len(password) >= 8

print("\nValidation Results:")
print(validator)
print("Minimum length valid:", length_valid)

# Final check
if (length_valid and
        validator['upper'] and
        validator['lower'] and
        validator['digit'] and
        validator['special'] and
        not validator['space']):

    print("\nPassword is Strong ✅")
else:
    print("\nPassword is Weak ❌")













