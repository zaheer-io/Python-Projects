read = open("file.txt", 'r')



#write a program to find the number of lines in a file

lines = read.readlines()

print(len(lines))

read.seek(0)

#write a program to find the number of words in a file

words = read.read()
# print(len(list(words.split())))

print(words)
print(words.split())
