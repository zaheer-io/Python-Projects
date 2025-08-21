print("----Students details----")
print("\n")

stdid = 0
stdname = ""
stmt = ""
studentlist = []

while True:
    stdid = int(input("Enter student id : "))
    stdname = input("Enter student name : ")
    print("\n")
    print("Enter marks: ")
    physics = chemistry = bilogy = maths = english = hindi = 0

    physics = int(input("Enter marks of Physics: "))
    chemistry = int(input("Enter mark of Chemisty: "))
    bilogy = int(input("Enter mark of Biology: "))
    maths = int(input("Enter mark of Maths: "))
    english = int(input("Enter mark of English: "))
    hindi = int(input("Enter mark of Hindi: "))

    studentlist.append({'id' : stdid, 'name' : stdname, 'marks' : [{'physics' : physics, 'Chemistry' : chemistry, 'Biology' : bilogy, 'Maths' : maths, 'English' : english, 'Hindi' : hindi}]})

    stmt = input("Add new student ? ('y for yes or 'n' for no): ").lower()
    if stmt == 'n':
        break
    elif stmt == 'y':
        print("add new student details....")
        print("\n")
    else:
        print("please enter y or n ")

print(studentlist)