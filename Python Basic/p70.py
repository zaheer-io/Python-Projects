"""

first set

What is the use of map(),filter() and reduce()
Function?Explain with example?(5 marks)

map
    map return an map object after applying the function to each element in the given sequence

    syntax : map(function, sequence)

eg:
    a = [1,2,3,4,5]

    print(list(map(lambda x : x ** 2, a)))

#output is [1, 4, 9, 16, 25]

Filter

    Filter returns a filtered object after applying the following function to each file

    syntax : filter(function, sequence)

    eg:

     a = [1,2,3,4,5]
    print(list(filter(lambda x : x % 2 == 0, a)))

Reduct

    Reduce function reduce the following sequence to a single value after appluing the function to each element

    synatax : functools.reduce(function, sequence)

Eg:
     a = [1,2,3,4,5]
    print(functools.reduce(lambda a,b : a + b, a))

"""
from functools import reduce
from itertools import count

"""

What are major datatypes in Python? Explain with example (5 marks)

Integer
    
    int - 3
    float - 3.15
    complex - 3 + 8 j
    
String
    
    collection of characters are called string
    name = "zaheer"
    
    operators in string
        index - []
        slice - [start : stop : step]
    
Sequence

    List 
        list are the hetrogenious collection of datas, list is ordered mutalbe and support duplicates
        
        Creating list using
            l = {}
            l = list()
        
        eg :  l = ['a',15, 'b' 'zaheer', 10, 3.156]
    
    Tuple
        Tuple is hetrogenious collection of data types , tuple is immutalbe menas we can't edit tuple values after creation and tuple is ordered
        
        Creating tuple using 
            t = ()
            t = tuple()
        
        eg : t = ('a' , 10, 20, 3.15, 'anjana)  

Map
    Dictinory
    
        Paires of key and values are called map
            
        Create Dictionary using
            d = {}
            d = dict()
    
        eg :  m = {'name' : 'zaheer', 'age' : 20}

set
    
    Set is hetrogenious data type element, set is mutable and set dont allow duplicates
    
    create of set using
    
    s = set()
    
    s = {10,'za',3.14}
    
Bool

    Boolean represent True and False values
    
    a = True
    b = False

None
    
    None data type represent no values 
    
    creating empty dict, list and tuple using
        l = []
        t = ()
        d = {}

"""


"""
Second set


What is Lambda Function?.Where it is used?(2 marks)

Lamda function is a anonymous funciton.
Lamda function create using lambda keyword
lamda file is defined without name

example:
    
sumNum = lambda a,b : a + b

print(sumNum(10,20)

"""


"""
Third set

"""

l = ["Python", "Is", "Great"]

str = ""

for i in l:
    str += i[0]

print(str)


"""
4 the set

"""
def word(sentence):
    words = sentence.split()
    result = {}

    for word in words:
        if word not in result:
            result[word] = {
                "length": len(word),
                "is_palindrome": word == word[::-1],
                "count": words.count(word)
            }
    return result

s = input("Enter the string: ")
print(word(s))



"""
Final set




"""

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
