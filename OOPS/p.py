#write a python program using class methods and looping  menu to manage student records
# 1. add student(rollno, name , marks)
# 2. dispaly all students
# 3. delete a student
# 4. update markof a student
# 5. search student by name
# 6. exit
from idlelib.colorizer import prog_group_name_to_tag

students = list()

class StudentsDetails:

    def __init__(self):
        self.stdName = input("Enter student name: ")
        self.stdRollNo = int(input("Enter roll no: "))

        self.marks = {
            'physics' : input("Enter marks of physics: "),
            'chemistry' : input("Enter  mark of chemistry: "),
            'biology' : input("Enter mark of Biology: "),
            'maths' : input("Enter marks of Maths: ")
        }

        print("Sccessfully added student details\n")

    def printStudent(self):
        print(f"Student name: {self.stdName}")
        print(f"Student Roll no : {self.stdRollNo}")

        for sub, mark in zip(self.marks.keys(), self.marks.values()):
            print(f"{sub} : {mark}")

        print("\n")

    def updateStudentMark(self):
        print("Student Mark update session: ")

        self.marks = {
            'physics': input("Enter marks of physics: "),
            'chemistry': input("Enter  mark of chemistry: "),
            'biology': input("Enter mark of Biology: "),
            'maths': input("Enter marks of Maths: ")
        }

        print("Marks update successfully\n")

    def deletestudent(self):
        students.remove(self)
        print("Student removed\n")


def findstudent(stdName):
    for i in students:
        if i.stdName == stdName:
            return i

    return None

while True:
    print("\n===== Student Record Menu =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Delete a Student")
    print("4. Update Marks of a Student")
    print("5. Search Student by Name")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    print("\n")

    if choice == "1":

        s = StudentsDetails()
        students.append(s)

    elif choice == "2":

        for i in students:
            i.printStudent()

    elif choice == "3":

        name = input("Enter the student name: ")
        std = findstudent(name)
        if std:
            std.deletestudent()
        else:
            print("Student not found")

    elif choice == "4":

        name = input("Enter the student name: ")
        std = findstudent(name)
        if std:
            std.updateStudentMark()
        else:
            print("Student not found")

    elif choice == "5":

        name = input("Enter the student name: ")
        std = findstudent(name)
        if std:
            std.printStudent()
        else:
            print("Student not found")

    elif choice == "6":
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice, please try again.")




