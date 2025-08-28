#read a sentence and find each word, length, count and is palindrome in the form of dictinoary

#{words : {length : 0, is_palindrome : True/False, count : 0}}

s = input("Enter the string: ")

words = s.split()
d = dict()

for i in words:
    d[i] =  {"length" : len(i), 'is_palindrome' : i == i[::1], 'count' : words.count(i)}

print(d)