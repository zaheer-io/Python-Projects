import functools

# # Beginner Level
#
# # Find the maximum element in the list using reduce.
# # 👉 Input: [12, -4, 78, -34, 90, 45, 16, 26, -2, -11, 3] → Output: 90
#
# l = [12, -4, 78, -34, 90, 45, 16, 26, -2, -11, 3]
#
# print(functools.reduce(lambda x, y : x if x > y else y, l))
#
# # Find the minimum element using reduce.
#
# print(functools.reduce(lambda x, y : x if x < y else y, l))
#
#
# # Square all positive numbers in the list using map.
# # 👉 Input: [1, -2, 3, -4] → Output: [1, 9] (only positives squared)
#
# l =  [1, -2, 3, -4]
#
# print(list(map(lambda x: x ** 2, filter(lambda x : x > 0, l))))
#
#
# # Cube all even numbers using map and filter.
# # 👉 Input: [2, 3, 4, 5] → Output: [8, 64]
#
# l = [2, 3, 4, 5]
#
# print(list(map(lambda x : x ** 3, filter(lambda x : x % 2 == 0, l))))

# # ✅ Intermediate Level
#
# # Count how many numbers are divisible by 3.
# # 👉 Input: [3, 6, 7, 9, 10] → Output: 3
#
# l = [3, 6, 7, 9, 10]
#
# print(len(list(filter(lambda x : x % 3 == 0, l))))
#
# # Find product of all positive numbers using reduce.
#
# print(functools.reduce(lambda x:, y : x * y, filter(lambda x : x > 0, l)))
#
# # Sort words by their length using sort(key=lambda...).
# # 👉 Input: ["apple", "cat", "banana", "dog"] → Output: ["cat", "dog", "apple", "banana"]
#
# l = ["apple", "cat", "banana", "dog"]
#
# l.sort(key=lambda x : len(x))
# print(l)
#
# # Reverse each string in a list using map.
# # 👉 Input: ["hello", "world"] → Output: ["olleh", "dlrow"]
#
# l = ["hello", "world"]
# print(list(map(lambda x : x[::-1], l)))




# ✅ Advanced Level

# Find the longest word in a list using reduce.
# 👉 Input: ["apple", "banana", "cherry", "date"] → Output: "banana"


l = ["apple", "banana", "cherry", "date"]

print((functools.reduce(lambda x, y : x if len(x) > len(y) else y, l)))

# Calculate factorial of a number using reduce.
# 👉 Input: 5 → Output: 120

#fact = functools.reduce(lambda x : )

# Find the sum of squares of all positive even numbers using map + filter + reduce.
# 👉 Input: [2, -3, 4, 5] → Output: 20 (since 2² + 4² = 4 + 16)

l = [2, -3, 4, 5]

print(functools.reduce(lambda x, y : x + y, map(lambda x : x ** 2, filter(lambda x : x > 0 and x % 2 == 0, l))))

# Group words by first letter (use sorted with key=lambda word: word[0]).
# 👉 Input: ["bat", "ball", "apple", "cat"] → Output: ["apple", "bat", "ball", "cat"]

l = ["bat", "ball", "apple", "cat"]

l.sort(key=lambda x : x[0])
print(l)



