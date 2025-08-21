#given string find the maximum length word
s = "python is a programming language"

large = ""
for i in s.split():
    if len(i) > len(large):
        large = i

print(f"Large word = {large} and length {len(large)}")



#find the maximum value fro the lsit without using max() function

l = [12,45,67,89,23]

large = 0

for i in l:
    if i > large:
        large = i

print(f"maximum value in the list {l} is {large}")