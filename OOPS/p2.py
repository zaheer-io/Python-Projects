class Employ:
    def __init__(self):
        self.empid = int(input("Enter emp id: "))
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.place = input("Enter Place: ")
        self.salary = int(input("Enter salary: "))
        self.designation = input("Enter designiation: ")

    def showdetails(self):
        print(self.empid, self.name, self.age, self.place, self.designation)

    def getsalary(self):
        print(self.salary)

e1 = Employ()

e1.showdetails()
e1.getsalary()