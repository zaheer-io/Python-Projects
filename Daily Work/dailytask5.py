
s1 = input("Enter first string: ") #zaheer
s2 = input("Enter second String: ") #reehaz

count = 0

def findcount(n, s):
    c = 0
    for i in s:
        if i == n:
            c += 1
    return c

for a, b in zip(s1, s2):
    if a in s1 and b in s2:
        if findcount(a, s1) == findcount(a, s2) and findcount(b, s1) == findcount(b, s2):
            count += 1

if count == len(s1) == len(s2):
    print("Done")
else:
    print("Not done")