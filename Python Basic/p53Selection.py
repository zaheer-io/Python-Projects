#Selection sort

n = int(input("Enter the limit: "))
l = [int(input(f"Enter the {i + 1} Element: ")) for i in range(n)]

print(f"Before sorting: {l}")

for i in range(n):
    min = i
    for j in range(i+1, n):
        if l[j] < l[min]:
            min = j

    l[min], l[i] = l[i], l[min]

print(f"After sorting : {l}")