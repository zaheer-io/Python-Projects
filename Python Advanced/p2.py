#wrtie a program to find a word in a file

# with open("new.txt", "r") as read:
#     print(read.read())
#     read.seek(0)
#
#     word = read.read()
#
#     n = input("Enter a word: ")
#
#     if n in word:
#         print("find")
#     else:
#         print("not found")

# with open("new.txt", "r") as read:
#     lines = read.readlines()
#     print(lines)
#
#     read.seek(0)
#
#     for i in range(-1,-6,-1):
#         print(lines[i])


# with open("file.txt", "r") as read:
#     print(read.read())
#
#     s = input("Enter new second line: ")


#write a program to find the number of letters digits and space inise the file

# with open("new.txt", "r") as read:
#     s = read.read()
#     news = list(s)
#
#     num = 0
#     letter = 0
#     space = 0
#     for i in news:
#         if i.isdigit():
#             num += 1
#         if type(i) == str:
#             letter += 1
#         if i == ' ':
#             space += 1
#
#     print(num, letter, space)


#wap to to change second line

with open("new.txt", "r") as read:
    l = read.readlines()
    print(l)

with open("new.txt" , "w") as write:
    write.writelines(l)


read.seek(0)
print(read.readlines())


