#sum of elements l = [11,23,56,34] print all 3 digit numbers

l = [11,23,56,34]
sum = 0

for i in l:
    sum += i

print("Sum of the elemtnts in the list = ", sum)

#print all 3 digit numbers

print("\n")

for i in range(100, 1000):
    print(i, end=" ")

print()

print("\n")

#given colours, colours = ['red', 'green', 'blue', 'black', 'orange']

colours = ['red', 'green', 'blue', 'black', 'orange']

for i in colours:
    if i[0] == "b":
        print(i)

