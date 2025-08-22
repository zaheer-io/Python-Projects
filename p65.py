# import functools
#
# l = [1,2,3,4,5]
#
# print(functools.reduce(lambda ))
import functools

phone_book={

    'john':['8592790000','john@gmail.com'],

    'Bob':['7994880000','bob@gmail.com'],

    'Tom':['9749552647','tom@gmail.com']

}



print(list(map(lambda x : x[1], phone_book.values())))


# count of floating point values

l=[10,'hello',9.8,'abc',11.2,'arun']
print(len(list(filter(lambda x : type(x) == float, l))))

print(functools.reduce(lambda a, b: a + (1 if isinstance(b, float) else 0), l, 0))
