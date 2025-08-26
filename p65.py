# # # s = "hello world"
# # #
# # # print(type(s))
# # # print(len(s))
# # # print(max(s))
# # # print(min(s))
# # #
# # # print(s.strip(""))
# # # print(s.split("l"))
# # # print("-".join(s))
# # #
# # # print(s.find("e"))
# # # print(s.index("e"))
# # # print(s.count("l"))
# # #
# # # print(s.startswith("h"))
# # # print(s.endswith("e"))
# # # print(s.isalnum())
# # # print(s.isalpha())
# # # print(s.islower())
# #
# # a = [10,20,30,40,50,60,70,80,90]
# #
# # print(a.index(20))
# # print(a.count(30))
# # print(type(a))
# # print(max(a))
# # print(min(a))
# # a.sort(reverse=True)
# # print(a)
# # print(a.reverse())
# # print(a.sort(key=lambda x : x > 50))
# import functools
#
# # Set 1: Basic Lambda Functions
# #
# # Medium (2):
# #
# # Write a lambda function that takes a number x and returns x^3 + 2x + 5.#
#
# # n = int(input("Enter a number: "))
# # ans = (lambda x : (x ** 3 ) + (2 * x) + 5)
# # print(ans(n))
#
#
# # Create a lambda function that checks whether a string has even length.
#
# # s = input("enter a sting: ")
# #
# # ln = lambda x : f"{s} is even" if len(x) % 2 == 0 else f"{s} is odd"
# # print(ln(s))
#
# # Hard (3):
# # 3. Use a lambda function to sort a list of strings by their last character.
#
# # l = ['apple', 'banana', 'orange', 'jack fruit']
# #
# # b = sorted(l, key=lambda x : (x[-1], x))
# # print(b)
#
# # 4. Write a lambda function that takes two numbers x and y and returns True if x is a multiple of y.
#
# # a = int(input("Enter first number: "))
# # b = int(input("Enter second number: "))
# #
# # ans = lambda x, y : True if x % y == 0 else False
# # print(ans(a,b))
#
# # 5. Write a lambda function that accepts a list of numbers and returns a new list with squared odd numbers only.
#
# # l = [1,2,3,4,5,6,7,8,9]
# #
# # print(list(map(lambda x : x ** 2, filter(lambda x : x % 2 != 0, l))))
#
#
#
#
# # Set 2: map() Function
# #
# # Medium (2):
# # 6. Use map() and a lambda to convert a list of temperatures in Celsius to Fahrenheit.
#
# # l = [23.6,45,23.6,89.1]
# #
# # print(list(map(lambda x : x * (9/5) + 32, l)))
#
# # 7. Use map() to add two lists element-wise: [1,2,3] and [4,5,6].
#
#
#
# # Hard (3):
# # 8. Given a list of strings ["apple", "banana", "cherry"], use map() to create a list of tuples containing (string, length_of_string).
#
# # l = ["apple", "banana", "cherry"]
# #
# # t = list(map(lambda x : (x, len(x)), l))
# # print(t)
#
# # 9. Use map() to convert a list of numbers to binary strings.
#
#
#
# # 10. Given ["python", "java", "c++"], use map() with a lambda to capitalize the first and last letters of each string.
#
# # l = ["python", "java", "c++"]
# #
# # a = list(map(lambda x : (x[0].upper()) + x[1:-1] + x[-1].upper() if len(x) > 1 else x.upper(), l))
# # print(a)
#
#
#
#
#
#
#
#
# # Set 3: filter() Function
# #
# # Medium (2):
# # 11. Use filter() to extract all numbers divisible by 5 from a list [10, 13, 25, 31, 50].
#
# # l = [10, 13, 25, 31, 50]
# #
# # print(list(filter(lambda x : x % 5 == 0, l)))
#
# # 12. Use filter() to get all strings longer than 4 characters from a list ["dog", "elephant", "cat", "tiger"].
#
# # l = ["dog", "elephant", "cat", "tiger"]
# #
# # print(list(filter(lambda x : len(x) > 4, l)))
#
# # Hard (3):
# # 13. Filter out all numbers which are prime from [2,3,4,5,6,7,8,9,10] using a lambda inside filter().
#
# # l = [2,3,4,5,6,7,8,9,10]
# #
# # print(list(filter(lambda x : all(x % i != 0 for i in range(2, x)), l)))
#
# # 14. Given a list of words, filter those which start and end with the same letter.
#
# # l = ['anjana', 'zaheer', 'muth', 'malayalam', 'her', 'zaaz']
# #
# # print(list(filter(lambda x : x[0] == x[-1], l)))
#
# # 15. From [1,2,3,4,5,6,7,8,9,10], filter numbers whose sum of digits is odd.
#
# # l = [11,24,30,41,57,69,72,83,90,104]
# #
# # print(list(filter(lambda x : sum(), l)))
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Set 4: reduce() & Higher-Order Combination
# #
# # Medium (2):
# # 16. Use reduce() to find the product of all numbers in [1,2,3,4,5].
#
# # l = [1,2,3,4,5]
# #
# # print(functools.reduce(lambda a,b : a + b, l))
#
# # 17. Combine map() and reduce() to find the sum of squares of [1,2,3,4].
# # l =[1,2,3,4]
# #
# # print(functools.reduce(lambda a,b : a + b , map(lambda x : x ** 2, l)))
#
# # Hard (3):
# # 18. Use reduce() to concatenate all strings in ["I","love","Python"] with a space between them.
#
# # l = ["I","love","Python"]
# #
# # print(functools.reduce(lambda a,b : a + " " + b, l))
#
# # 19. Given [1,2,3,4,5], use reduce() to find the maximum difference between consecutive elements.
#
# l = [1, 3, 2, 8, 5]
#
# print(functools.reduce(lambda a,b : a - b , filter(lambda x : , l)))
#
#
#
# # 20. Use map(), filter(), and reduce() together to find the sum of squares of all odd numbers less than 20.