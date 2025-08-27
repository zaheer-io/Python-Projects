# Normal
#
# Write a function that returns the middle character(s) of a string. For even length, return the two middle chars.
from itertools import count

from p48 import index

# s = input("enter the string: ")
# l = len(s)
#
# if len(s) % 2 == 0:
#     print(s[l//2 - 1], s[l//2])
# else:
#     print(s[l//2])

# Given s, print the first and last characters and also s[0:5], s[-3:]. Explain outputs.

# s = input("enter a sting: ")
# print(s[0]) #first character
# print(s[-1]) #last character
#
# print(s[0:5]) #start character to 5th character
# print(s[-3:]) #thirrd last character to last character

# Reverse a string using slicing only (no loops).

# s = "hello world"
# print(s[::-1])

# Count vowels/consonants in a string (ignore case, treat non-letters separately).

# vowels = ['a', 'e', 'i', 'o', 'u']
#
# s = input("enter a string: ")
# countv = 0
# counts = 0
#
# for i in s.lower():
#     if i in vowels:
#         countv += 1
#     else:
#         counts += 1
#
# print(f"No of vowels is {countv} and no of consonants is {counts}")

# Given a sentence, capitalize the first letter of each word without using title().

s = input("Enter the sentence: ")

slist = list(s)
print(slist)

for i in slist:
    if index(i) == 1:
        i.upper()

print(slist)



#
# Hard
# 6) Implement a function that removes all duplicate characters but preserves first occurrences and original order.
# 7) Split a CSV line that may contain quoted commas (e.g., "a,1","b,2",c). Do not use csv module.
# 8) Given s, build a frequency dict of characters, then print chars sorted by frequency desc, then alphabetically.
# 9) Implement startswith_any(s, prefixes) and endswith_any(s, suffixes) without using built-ins.
# 10) Given two strings, compute the longest common substring (contiguous) and return it.
#
# Extreme
# 11) Write a mini template engine: replace placeholders like {{name}} using a dict; support default {{name|Guest}}.
# 12) Normalize whitespace: collapse runs of spaces/tabs/newlines into a single space, but keep punctuation attached.
# 13) Implement basic wildcard matching with ? and * (like glob) using DP; return True/False.
# 14) Encode and decode run-length encoding (RLE) for strings (e.g., aaabb → a3b2).
# 15) Detect if a string is a valid Python identifier (per rules), without using .isidentifier().