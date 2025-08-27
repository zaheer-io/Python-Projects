#Given a dictionary
employee={
    "id":101,
    "name":"Anjali",
    "department":"HR",
    "salary":450000
}

#Print the department of employee
#Updates the salary to 50000
#print the updated salary
#Add a new key -value pair location:Bangalore to employee

print("\n\nFirst question")

print("Department of employee ", employee.get('department'))

employee['salary'] = 50000

print("Updated salary = ", employee.get('salary'))

employee.update({'location' : 'Bangalore'})
print("Updated location = ", employee)

print("\n\n-------------------------------")


#Given a string
msg="Hello, Python World!"

#print the first character
#print the last character
#print the first 5 characters
#print the reverse
#print the length

print("\n\nSecond question")

print("First letter of the character = ", msg[0])

print("The last lettr fo the character = ", msg[-1])

print("First five characters = ", msg[0:5])

print("Reverse order =", msg[::-1])

print("Length of the string = ", len(msg))

print("\n\n----------------------------------")

#Given a set
s={'dog','cat','rabbit','cow'}
#add a new animal "lion" to set
#print the updated set

print("\n\nThird question")

print("Current set = ", s)

s.add("lion")
print("Updated set = ", s)

print("\n\n----------------------")

#Given a list
l=['Riya',"Ankit","Sara","Manu"]


#Print the first student
#Changes the second value to Amit

#Add a new student Amal
#Print the length
#print the updated list


print("\n\nFourth question")

print("First student = ", l[0])

l[1] = "Amit"
print("Updated list = ", l)

l.append("Amal")
print("Updated list = ", l)

print("Length of the lsit = ", len(l))

print("Final updated list = ", l)

print("\n\n----------------------")


#5 key features of Python

#What is the difference between mutable and immutable type?Give example

#What are the Major datatypes in Python?

print("\n\nQuestions")

print("\nI. Key features of python\n")
print("1. Python is a high level language. \n2. Python is multipurpose language (used in AI, data science, machine learning etc..) \n3. Python is interpreter language (interceptor is used to convert high level programming language to low level.\n4. Large community support. \n5. Large library support. \n6. Multi program paradigms (python act as both procedural oriented language and object oriented language) \n7. Easy syntax")

print("\n\nII. Difference betewen mutable and immutable language\n")
print("Mutable type we can edit there values eg: set, dictionary, list \n In immutable type we cant change there vlaues after assign eg: string, tuple")


print("\n\nIII. Major datatypes of python\n")
print("1. Numeric type(eg : int(1,2,3,4), float(1.2,0.36,2.3) and complex(5+3j) . \n2. Text type (eg : string). \n3. Sequence type(eg : set, tuple). \n4.Mapping type(eg : dictionary). \n5. Sets type (eg : sets). \n6. Boolean type (eg : ture or false). \n7. None type")