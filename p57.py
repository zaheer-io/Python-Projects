"""

#find the position of a specific character in a string

s = "python is a programming language"

ch = input("Enter a character: ")

print(f"Position of {ch} in '{s}' is {s.index(ch)}")


c = input("Enter the character: ")
print(f"Count of {c} in '{s}' is {s.count(c)}")

create a dict where keys are charater ad fom the string and value are count of each character

s = "hello world"

cdict = {i : s.count(i) for i in s if i != " "}
print(cdict)
"""

#print the word whose length is greater than 5
s = "python coding is easy and fun"

for i in s.split():
    if len(i) > 5:
        print(i)