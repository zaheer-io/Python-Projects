from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self):
        self.empid = int(input("Enter employee id: "))
        self.empname = input("Enter employee name: ")
        self.age = int(input("Enter age: "))

    @abstractmethod
    def get_salary(self):
        pass

class FixedHourEmployee(Employee):
    def fixed(self):
        self.salary = int(input("Enter the salary: "))

    def get_salary(self):
        print(self.salary)

e = FixedHourEmployee()
e.fixed()
e.get_salary()
