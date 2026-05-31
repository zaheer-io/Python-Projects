# # Q26.
# # Write a function to check palindrome.
#
# def check_palindrome(string):
#     return string == string[::-1]
#
# # Q27.
# # Write code to find second largest number in a list.
#
# def second_largest(num):
#     unique = list(set(num))
#     scr = sorted(unique)
#     return scr[-2]
#
#
#
# # Q28.
# # Write code to count vowels in a string.
#
# vowels = 'aeiou'
#
# def count_vowels(string):
#     count = 0
#     for c in string.lower():
#         if c in vowels:
#             count += 1
#
#     return count
#
#
# # Q29.
# # Write code to swap two numbers without third variable.
#
# def swap_numbers(num1, num2):
#      num1, num2 = num2, num1
#      return num1, num2
#
#
# # Q30.
# # Write a function to check prime number.
#
# from math import sqrt
#
# def prime_number(num):
#     is_prime = True
#
#     if num == 1 or num == 0:
#         is_prime = False
#         return is_prime
#     for i in range(2, num-1):
#         if num % i == 0:
#             is_prime = False
#             break
#     return is_prime



def find_kth_largest(nums, k):


    nk = len(nums) - k
    num_sort = sorted(nums)
    print(num_sort[nk])

numsList = [1, 3, 4,2,7,7,9,12,4]
kth = int(input('Enter the kth largest number: '))

find_kth_largest(numsList, kth)





















