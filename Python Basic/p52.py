"""
def add(n1, n2):
    sum = n1 + n2
    print(sum)

add(10,20)

def add(a, b):
    sum = a + b
    print(sum)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add(a, b)

"""


#write a function to find the simple interest


#define a function to find the count of a specific character in a string using parameters and arguments

def find_char(string, character):
    count = 0
    for i in string:
        if character == i:
            count += 1
    print(count)

word = input("Enter the string: ")
char = input("Enter the character: ")

find_char(word, char)
