l = ['kelly', 'emy', 'alen']

for i in l:
    for j in l:
        print(i, end=" ")
    print()

print("\n\n")

for i in range(1, 4):
    print(i)
    for j in range(1, 4):
        print(j, end=" ")
    print()

print("\n\n")

for i in range(1, 5):
    print("* " * i)

print("\n\n")

for i in range(4, 0, -1):
    print("* " * i)

print("\n\n")

for i in range(1, 5):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

print("\n\n")

for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()


print("\n\n")


for i in range(2, 9, 2):
    print("* " * i)

print("\n\n")


for i in range(2, 9, 2):
    for j in range(i):
        print("* " , end= " ")
    print()

print("\n\n")

for i in range(1, 8, 2):
    for j in range(i):
        print("* " , end= " ")
    print()
