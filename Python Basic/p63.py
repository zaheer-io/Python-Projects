from functools import reduce

l = [12,-4,78,-34,90,45,16,26,-2,-11,3]

#sum of positive even numbers

print(reduce(lambda a,b : a + b, filter(lambda x : x > 0 and x % 2 == 0, l)))

#sum of positive odd numbers

print(reduce(lambda a, b : a + b, filter(lambda x : x > 0 and x % 2 == 1, l)))

#sum of negative even numbers

print(reduce(lambda a, b : a + b, filter(lambda x : x < 0 and x % 2 == 0, l)))

#sum of negative odd numbers

print(reduce(lambda a,b : a + b, filter(lambda x : x < 0 and x % 2 == 1, l)))


#count of postitive numbers

print(len(list(filter(lambda x : x > 0, l))))

#cont of negative numbers

print(len(list(filter(lambda x : x < 0, l))))

#count of even numbers

print(len(list(filter(lambda x : x % 2 == 0, l))))

#new clone to pycharm

