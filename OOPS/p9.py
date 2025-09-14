class Company:
    def __init__(self):
        self.companyName = input("Enter company name: ")

    def showCompanyName(self):
        print(f"Company name: {self.companyName}")

class Employee(Company):
    def __init__(self):
        super().__init__() #or Company.__init__(self)
        self.empName = input("Enter employee name: ")
        self.empAge = int(input("Enter employee age: "))
        self.empid = int(input("Enter employee id: "))
        self.empsalary = int(input("Enter employee salary: "))

    def showEmployeeDetails(self):
        print(f"Employee id: {self.empid}")
        print(f"Employee name: {self.empName}")
        print(f"Employee Age: {self.empAge}")
        super().showCompanyName() #or Company.showCompanyName(self)
        print(f"Employee Salary: {self.empsalary}")

    def getSalary(self):
        print("Employee salary: ", self.empsalary)

obj = Employee()
print("\n")
obj.showCompanyName()
print("\n")
obj.showEmployeeDetails()
print("\n")
obj.getSalary()