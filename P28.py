# 🔁 Level 2: List Manipulation Without .append()
# Reverse the list without using .reverse() or slicing ([::-1])
#
# Create a list of the first letter of each name
#
# Select names at even indices but in reverse order
#
# Join two lists of names together using +
#

"""
names = ['arya' , 'anjana', 'muth', 'appus', 'sini', 'zaheer', 'laya']

revlist = []
j = 0
for i in names:
    revlist.insert(len(revlist) - j, i)
    j += 1

print(revlist)


temp = ""
fltrlist = []

for k in names:
    temp = k
    fltrlist.append(temp[0])

print(fltrlist)


evenrevlist = []


for l in range((len(names) - 1), -1, -2):
    evenrevlist.append(names[l])

print(evenrevlist)

print(names + evenrevlist)

"""


# 🧠 Level 3: Slightly Tricky
# Collect names that contain double letters (like ‘appus’)
# You’ll have to check for consecutive repeating characters.
#
# Make a list of name lengths for each name
# Eg: ['arya', 'anjana'] → [4, 6]
#
# Without using .append(), collect names whose index is divisible by 3
#
# Create a list of tuples where each tuple is (index, name)
# Example: [(0, 'arya'), (1, 'anjana')]
#

names = ['arya' , 'anjana', 'muth', 'appus', 'sini', 'zaheer', 'laya']

letter = []

for i in names:
    for j in range(0, len(i) - 1):
        if i[j] == i[j + 1]:
            letter.append(i[j])

print(letter)



# 🧪 Bonus: Challenge Yourself
# Given a list of numbers, collect only those that are perfect squares.
#
# Without .append() or list comprehension, build a list of squares of even numbers from another list.
#
# Create a new list that has the names in alternating uppercase and lowercase (first upper, second lower, etc.)