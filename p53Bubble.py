#Bubble sort

n = int(input("Enter the limit of the list: "))
l = []

for i in range(0, n):
    e = int(input(f"Enter {i + 1} element: "))
    l.append(e)

print(f"Befor sorted: {l}")


for i in range(0, len(l)):
    for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

print(f"After sorted: {l}")





