# p.py
# Detailed inferred question:
# - Read a sentence and create dictionary:
#   `{word: {'length': len(word), 'is_palindrome': bool, 'count': frequency}}`.
from functools import reduce
from os.path import split

# string = input('Enter the string: ')
#
# wordDict = {}
#
# for word in string.split():
#     wordDict.update({
#         word : {
#             'length' : len(word),
#             'is_palindrome' : word == word[::-1],
#             'count' : string.count(word)
#         }
#     })
#
# print(wordDict)



# p1.py
# Detailed inferred question:
# - Read sentence and build per-word dictionary including:
#   `length`, `count`, `is_palindrome`, `number_of_vowels`, `number_of_consonants`.


#
# string = input('Enter the string: ')
#
# wordDict = {}
#
# vowels = 'aeiou'

# def count_vowels(word):
#     count = 0
#     for ch in word.lower():
#         if ch in vowels:
#             count +=1
#     return count
#
# def count_consonants(word):
#     count = 0
#     for ch in word.lower():
#         if ch.isalpha() and ch not in vowels:
#             count += 1
#     return count

# for word in string.split():
#     wordDict.update({
#         word : {
#             'length' : len(word),
#             'count' : string.count(word),
#             'is_palindrome' : word == word[::-1],
#             'number_of_vowels' : len(list(filter(lambda x : x in vowels, word))),
#             'number_of_consonants' : len(list(filter(lambda x : x not in vowels, word)))
#         }
#     })
#
# print(wordDict)


# p2.py
# Detailed inferred question:
# - Read string, ignore spaces, and create character dictionary:
#   `{char: {'count': n, 'is_vowel': bool, 'ascii': ord(char)}}`.

# string = input('Enter the string: ')
#
# vowels = 'aeiou'
#
# chrDict ={}
#
# print(''.join(string))
#
# for ch in ''.join(string.split()):
#     chrDict.update({
#         ch : {
#             'count' : string.count(ch),
#             'is_vowel' : ch in vowels,
#             'ascii' : ord(ch)
#         }
#     })
#
# print(chrDict)

# p3.py
# Detailed inferred question:
# - Input student name and marks as comma-separated text.
# - Build nested dictionary:
#   `{name: {'marks': score, 'grade': A/B/C/D/F, 'pass': True/False}}`.

# name = input('Enter the name: ')
# marks = list(map(lambda x : int(x), input('Enter student marks as coma-separated: ').split(',')))
#
# stdDetails = {}
#
# def findGrade(score):
#     if score > 80 and score < 100:
#         return 'A'
#     elif score > 60:
#         return 'B'
#     elif score > 40:
#         return 'C'
#     elif score > 20:
#         return 'D'
#     else:
#         return 'E'
#
# stdDetails.update({
#     name : {
#         'marks' :( totalScore := (sum(marks)) / len(marks)),
#         'grade' : findGrade(totalScore),
#         'pass' : findGrade(totalScore) != 'E'
#     }
# })
#
# print(totalScore)
# print(stdDetails)



# p4.py
# Detailed inferred question:
# - Given list of tuples
#   `[("apple",3), ("banana",5), ("apple",2), ("orange",1)]`,
#   convert into merged dictionary count format.
#

# fruits = [("apple",3), ("banana",5), ("apple",2), ("orange",1)]
# fruitDict = {}
#
# for name, count in fruits:
#     fruitDict.update({
#         name : count
#     })
#
# print(fruitDict)



# p6.py
# Detailed inferred question:
# - Parse employee data string
#   `"101,John,HR,35000;102,Ana,IT,55000;103,Sam,Sales,45000"`
#   into nested dictionary keyed by employee id.


# emp = "101,John,HR,35000;102,Ana,IT,55000;103,Sam,Sales,45000"
#
# empData = emp.split(';')
# print(empData)
#
# empList = list(map(lambda x : tuple(x.split(',')), empData))
# print(empList)
#
# empDict = []
#
# for id, name, des, salary in empList:
#     empDict.append(
#         {
#             'emp_id': id,
#             'emp_name': name,
#             'emp_designation': des,
#             'emp_salary': salary
#         }
#     )


# p8.py
# Detailed inferred question:
# - Read comma-separated numbers and build dictionary:
#   `{num: {'square': num**2, 'cube': num**3, 'iseven': bool, 'isodd': bool}}`.


# numList = list(map(lambda x : int(x), input('Enter the numbers coma-separated: ').split(',')))
# print(numList)
#
# numDict = {}
#
# for num in numList:
#     numDict.update({
#         num : {
#             'square' : num ** 2,
#             'cube' : num ** 3,
#             'is_even' : num % 2 == 0,
#             'is_odd' : num % 2 != 0
#         }
#     })
#
# print(numDict)


# p9.py
# Detailed inferred question:
# - Given `keys=["a","b","c"]` and `values=[10,20,30]`, create forward mapping dictionary and also reverse mapping.

#
# keys=["a","b","c"]
#
# values=[10,20,30]
#
# forwardDict = {}
#
# for key, value in zip(keys, values):
#     forwardDict.update({
#         key : value
#     })
#
# print(forwardDict)
#
# backwardDict = {}
#
# for key, value in zip(list(reversed(keys)), list(reversed(values))):
#     backwardDict.update({
#         key : value
#     })
# print(backwardDict)
#

# p15.py
# Detailed inferred question:
# - Merge dictionaries `d1={"a":2,"b":3}` and `d2={"a":5,"c":10}`
#   to output `{"a":7,"b":3,"c":10}`.
#   (File currently incomplete.)



# d1={"a":2,"b":3}
#
# d2={"a":5,"c":10}
#
# dataList = list(d2.items()) + list(d1.items())
# print(dataList)
#
#
# d3 = {}




# Dailytask2.py
# Detailed inferred question:
# - Print the following 6-row pattern using loop logic where row number multiples of 3 are stars:
#   1
#   22
#   ***
#   4444
#   55555
#   ******



# k = 0
# for i in range(1, 7):
#     k +=1
#     if k % 3 == 0:
#         print('*' * i)
#     else:
#         print(f'{i}' * i)


# k = 0
#
# for i in range(1, 7):
#     k += 1
#     for j in range(1, i + 1):
#         if k % 3 == 0:
#             print('*', end='')
#         else:
#             print(i, end='')
#     print()

# DailyTask3.py
# Detailed inferred question:
# - Print a 7-row binary triangle pattern where odd rows start with `1` and even rows start with `0`, then alternate within the row.
#   Example row style:
#   Row1: `1`
#   Row2: `0 1`
#   Row3: `1 0 1`

# e = 0
# o = 1
#
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if i % 2 != 0:
#             if j % 2 != 0:
#                 print(o, end=' ')
#             else:
#                 print(e, end=' ')
#         else:
#             if j % 2 != 0:
#                 print(e, end=' ')
#             else:
#                 print(o, end=' ')
#     print()




# DailyTask4.py
# Detailed inferred question:
# - Read two integers from input and print their sum directly in one expression.


# print(f"sum is {int(input('Enter first number: ')) + int(input('Enter second number: '))}")
#
#


# DailyTask5.py
# Detailed inferred question:
# - Given digit-word list
#   `['zero','one','two','three','four','five','six','seven','eight','nine']`,
#   read an integer (e.g., `507`) and build a dictionary mapping each digit to its word
#   (e.g., `{5:'five', 0:'zero', 7:'seven'}`).




# alphaDigit = ['zero','one','two','three','four','five','six','seven','eight','nine']
#
#
# numDict = {}
#
# num = int(input('Enter a number: '))
#
# numList = list(map(lambda x : int(x), list(str(num))))
#
# print(numList)
#
# for n in numList:
#     numDict.update({
#         n : alphaDigit[n]
#     })
#
# print(numDict)

























