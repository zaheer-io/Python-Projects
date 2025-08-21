import functools
from itertools import count

l = [12,-4,78,-34,90,45,16,26,-2,-11,3]

print("Sum of the list ",functools.reduce(lambda x,y : x + y, l))
print()
#sum of positive even numbers

print("Sum of positive even numbers ",functools.reduce(lambda x, y : x + y, filter(lambda x: x % 2 == 0 and x > 0, l)))

#sum of positive odd numbers

print("Sum of positive odd numbers ",functools.reduce(lambda x, y : x + y, filter(lambda x : x % 2 == 1 and x > 0, l)))
print()

#sum of negative even numbers

print("Sum of negative even numbers ",functools.reduce(lambda x, y : x + y, filter(lambda x : x % 2 == 0 and x < 0, l)))

#sum of negative odd numbers

print("Sum of negative odd numbers",functools.reduce(lambda x,y : x + y, filter(lambda x : x % 2 == 1 and x < 0, l)))
print()

#count of postitive numbers

print("count of positive numbers ",len(list(filter(lambda x : x > 0, l))))

#cont of negative numbers

print("Count of negative numbers ",len(list(filter(lambda x : x < 0, l))))
print()

#count of even numbers

print("Count of even numbers ",len(list(filter(lambda x : x % 2 == 0, l))))

