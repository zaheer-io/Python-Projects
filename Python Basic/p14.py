#write a program to find the enter no is positve

# num1 = int(input("Enter a number : "))
# if num1 %2 == 0 :
#         print("Even")

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 4 == 0:
        print(num)


#write a program to diaplay a name if the entered name contains letter 'n'

name = input("Enter your name: ")

if 'n' in name:
        print("found")

#wap do display the name if the first character is 'a'

if name[0] == 'a':
        print(name)

#wap to display the name if the last character of name is 'a'

if name[-1] == 'a':
        print(name)

#wap to display a location if 'location' contains word 'land'

land = input("Enter the location: ")

if 'land' in land:
        print(land)