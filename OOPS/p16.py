#1. add employee,
# 2. salary details of a perticular employ,
# 3.

from abc import ABC, abstractmethod

emp_details = list()

class Employee(ABC):
    def __init__(self):
        self.empid = int(input("Enter employee id: "))
        self.empname = input("Enter employee name: ")
        self.age = int(input("Enter age: "))

    @abstractmethod
    def get_salary(self):
        pass

class Fixed(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.monthly_salary = int(input("Enter monthly salary: "))

    def get_salary(self):
        print(f"Employee id: {self.empid}")
        print(f"Employee name: {self.empname}")
        print(f"Employee salary: {self.monthly_salary}")


class Hourly(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.hour =  int(input("Enter hours: "))
        self.rate = int(input("Enter Rate: "))

    def get_salary(self):
        print(f"Employee id: {self.empid}")
        print(f"Employee name: {self.empname}")
        print(f"Total salary: {self.hour * self.rate}")


def find_emp(eid):
    for i in emp_details:
        if i.empid == eid:
            return i
    return None

while True:
    print("Menu")
    print("1. Add employee: ")
    print("2: Salary details of a employee using Employee id: ")
    c = int(input("Enter the choice: "))
    print("\n")

    match c:
        case 1:
            etype = int(input("choose Employee type '1' for fixed and '2' for Hourly: "))
            if etype == 1:
                fixed = Fixed()
                print("\n")
                emp_details.append(fixed)
            if etype == 2:
                hour = Hourly()
                print("\n")
                emp_details.append(hour)

        case 2:
            eid = int(input("Enter the employee id: "))
            print("\n")
            e = find_emp(eid)
            e.get_salary()

        case _:
            print("Enter valid choice...!")



