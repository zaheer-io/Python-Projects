# # # # for i in range(1, 100):
# # # #     print(i)
# # #
# # # n = int(input('Enter a nubmer: '))
# # # if n % 2 == 0:
# # #     print('even')
# # # else:
# # #     print('Odd')
# #
# # a = int(input())
# # b = int(input())
# # c = int(input())
# #
# # if a > b:
# #     if a > c:
# #         print(f'{a} is greatest')
# #     else:
# #         print(f'{b} is greatest')
# # else:
# #     if b > c:
# #         print(f'{b} is greatest')
# #     else:
# #         print(f'{c} is greatest')
#
#
# word = input('Enter the string: ')
# rev = ''
#
# for x in word:
#     rev = x + rev
#
# print(rev)

# from math import isqrt
#
# n = int(input())
#
# if n < 2:
#     print(f'{n} is not prime')
# else:
#     prime = True
#     for i in range(2, isqrt(n) + 1):
#         if n % i == 0:
#             prime = False
#             break
#
#     if prime:
#         print(f'{n} is prime')
#     else:
#         print(f'{n} is not prime')


# a, b = 0, 1
#
# n = int(input('Enter: '))
# for i in range(n+1):
#     print(a)
#     a, b = b, a+b

# word = input('Enter the string: ')
#
# countlet = {
#     'vowels' : 0,
#     'consonants' : 0
# }
#
# for x in word:
#     if x.lower() in 'aeiou' and x.isalpha():
#         countlet['vowels'] = countlet.get('vowels', 0) + 1
#     elif x.lower() not in 'aeiou' and x.isalpha():
#         countlet['consonants'] = countlet.get('consonants', 0) + 1
#
# print(countlet)

# from functools import reduce
#
# num_list = [2, 2, 2, 2, 2, 2]
#
# sumList = reduce(lambda a, b : a + b, num_list)
# print(sumList)

# word = input('Enter th string: ')
#
# freq = {}
#
# for x in word:
#     freq[x] = freq.get(x, 0) + 1
#
# print(freq)

