l = [25,16,89,84,54,12,4,36,17,83]

#create a list of even values

print(list(filter(lambda x : x % 2 == 0, l)))

#create a list of numbers that are divisible by 3

print(list(filter(lambda x : x > 50, l)))

#create a list that are divisibe by 3

print(list(filter(lambda x : x % 3 == 0, l)))

#create a list of even numbers greater than 50

print(list(filter(lambda x : x % 2 == 0 and x > 50, l)))