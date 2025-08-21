# Select every third name from a list
# Given names = ['arya', 'anjana', 'muth', 'appus', 'sini', 'zaheer', 'laya'],
# Create a new list skipped_names with every 3rd element.
#
# Copy only names with length greater than 4
# Without using .append(), collect names with more than 4 letters into a new list.
#
# Convert all names to uppercase using list comprehension
#
# Print names that start with a vowel


names = ['arya' , 'anjana', 'muth', 'appus', 'sini', 'zaheer', 'laya']
newnames3 = []
newnames2 = []

for i in range(0, len(names), 3):
    newnames3.append(names[i])

print(newnames3)

for j in range(0, len(names), 2):
    newnames2 = newnames2 + [names[j]]

print(newnames2)


length4 = []

for k in names:
    if len(k ) > 4:
        length4 = length4 + [k]

print(length4)

uppernames = []

for l in names:
    uppernames.append(l.upper())

print(uppernames)

vowel = ['a', 'e', 'i', 'o', 'u']

vowelnames = []

temp = ""

for m in names:
    temp = m
    print(temp)
    if temp[0] in vowel:
        vowelnames.append(temp)

print(vowelnames)


