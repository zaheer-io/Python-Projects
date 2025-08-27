#create a list of cubes from the list
l = [1,2,3,4]

print(list(map(lambda x : x ** 3, l)))

#create a list of names
l = [{'name' : 'arun', 'age' : 23}, {'name' : 'amal', 'age' : 24}, {'name' : 'anu', 'age' : 26}]

print(list(map(lambda x : x['name'], l)))

#create a list of authors

l = [['book1', 'john'], ['book2', 'mike', 300], ['name', 'sam', 500]]

print(list(map(lambda x : x[1], l)))

#create a list of length
colours = ['red', 'orange', 'green', 'yellow', 'blue']

print(list(map(lambda x : len(x), colours)))

#create of list of square roots
l = [36,81,49,16]

print(list(map(lambda x : x ** 0.5, l)))
