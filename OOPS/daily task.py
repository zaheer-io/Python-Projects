
s1 = input("Enter first string: ")
s2 = input("Enter second String: ")

count = 0
counts2 = 0


def findcount(n):
    c = 0
    for i in n:
        c += 1
    return c


for a, b in zip(s1, s2):
    if a in s2 and b in s1:
        count += 1

# print(findcount(s1))

if count == findcount(s1) == findcount(s2):
    print("Anagram")
else:
    print("Not anagram")