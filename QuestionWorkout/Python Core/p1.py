#write a program to find a word in a file
# f=open('text.txt','r')
# s=f.read()
# n=input('enter word')
# split=s.split()
# for i in split:
#     if n in i:
#         print('present')
#         break
#     else:
#         print('absent')
#         break


#write a program to print the last 5 lines from the file
# f=open('new.txt','r')
# s=f.readlines()
# print(s[-5::])

# #write a program to find the no. of letters,digits and spaces inside a file
# f=open('new.txt','r')
# s=f.read()
# count_l=0
# count_d=0
# count_s=0
# for i in s:
#     if(i.isalpha()):
#         count_l+=1
#     elif(i.isdigit()):
#         count_d+=1
#     elif(i.isspace()):
#         count_s+=1
#     else:
#         pass
#
# print(count_l,count_d,count_s)

#write a program to change the second line inside a file
f=open('new.txt','r')
s=f.readlines()
print(s) #read the existing file

s[1]="line is changed\n"
print(s)    #updated the 2nd line of the file

f=open('new.txt','w')
f.writelines(s) #write the line to the text file