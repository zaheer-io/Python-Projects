#pritn the string upto a specific character including that character

s = "python is a programming language"

ch = input('Enter a character: ')
for i  in s:
    print(i, end="")
    if i == ch:
        break


print("\n")

fruits = ['banana', 'apple', 'orange', 'pineapple', 'mango']
#iterate through the sequence and print each fruit name . exit the loop if fruit name = "pineapple"

for i in fruits:
    if i == "pineapple":
        break
    print(i, end=" ")
print()

print("\n")
#iterate through the sequence and print each fruit name . skip iteration if fruit name = "apple"

for i in fruits:
    if i == "apple":
        continue
    print(i, end=" ")
print()


print("\n")
#given a list print all elements except multiple of 3 using continue
l = [45,67,12,90,78,10]

for i in l:
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()


print("\n")
#given print the first occurence of colorname starting with 'b'
colours = ['red', 'green', 'orange', 'blue', 'black', 'yellow']

for i in colours:
    if i[0] == 'b':
        print(i)
        break

