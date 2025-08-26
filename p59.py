#given string find the maximum length word
s = "python is a programming language"

large = ""

for i in s.split():
    if len(i) > len(large):
        large = i

print(large)

#find the maximum value fro the lsit without using max() function

l = [12,45,67,89,23]

maxx = 0

for i in l:
    if i > maxx:
        maxx = i
print(maxx)