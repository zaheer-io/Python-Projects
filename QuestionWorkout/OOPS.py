# p3.py
# Detailed inferred question:
# - Create class `Books` with attributes:
#   `bookid`, `title`, `author`, `page`, `price`, `language`.
# - Implement methods:
#   `getauthor`, `gettitle`, `getprice`, `setauthor`, `settitle`, `setprice`.
# - Show old vs updated values when setter runs.

# class Books:
#     def __init__(self):
#         self.book_id = int(input('Enter book id: '))
#         self.title = input('Enter the book title: ')
#         self.author = input('Enter the book author: ')
#         self.page = int(input('Enter the book pages: '))
#         self.price = int(input('Enter the book Price: '))
#         self.language = input('Enter the book Language: ')
#
#     def get_author(self):
#         print(f'Author name is : {self.author}')
#
#     def get_title(self):
#         print(f'Title name is : {self.title}')
#
#     def get_price(self):
#         print(f'Book price is {self.price}')
#
#     def set_author(self):
#         oldAuthor = self.author
#         newAuthor = input('Enter the new Author: ')
#         self.author = newAuthor
#         print(f'Author name {oldAuthor} changed to {newAuthor}')
#
# book = Books()
# book.get_author()
# book.get_title()
# book.get_price()
# book.set_author()
# book.get_author()



# p4.py
# Detailed inferred question (commented block):
# - Create `Circle` class with `radius`; print area and perimeter using `math.pi`.

# from math import  pi
#
# class Circle:
#     def __init__(self):
#         self.radius = int(input('Enter the radius: '))
#
#     def find_area(self):
#         print(f'Area of circle is {round(pi * (self.radius ** 2), 2)}')
#
#     def find_perimeter(self):
#         print(f'Perimeter of circle is {(2 * pi * self.radius):.2f}')
#
# circle = Circle()
# circle.find_area()
# circle.find_perimeter()


# p4.py
# Detailed inferred question (active block):
# - Create `Bank` class with `accountno`, `name`, `balance`.
# - Implement `showbalance`, `deposit(amount)`, and `withdrawn()` with insufficient balance check.

#
# class Bank:
#     def __init__(self):
#         self.account_no = int(input('Enter the account no: '))
#         self.name = input("Enter the account Holder name: " )
#         self.balance = 0
#
#     def show_balance(self):
#         print(f'Current Balance is : {self.balance}')
#
#     def deposit(self):
#         amount = int(input('Enter Amount to Deposit: '))
#         self.balance += amount
#         print(f'New balance is {self.balance}')
#
#     def withdraw(self):
#         amount = int(input('Enter Amount to withdraw: '))
#         if amount > self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance += amount
#             print(f'New balance is {self.balance}')
#
#
# bank = Bank()
# bank.show_balance()
# bank.withdraw()
# bank.deposit()
# bank.withdraw()
# bank.deposit()


#
# p5.py
# Detailed inferred question:
# - Build menu-driven bank system with random account numbers (`1000`-`9999`) and initial balance `0.00`.
# - Features:
#   1) Create account by name
#   2) Deposit amount
#   3) Withdraw amount
#   4) Show balance
#   5) Exit


#
# import random
#
#
# accounts = []
#
# class Bank:
#     def __init__(self, name):
#         self.account_no = random.randint(0000, 9999)
#         self.name = name
#         self.balance = 0.00
#
#         print('Account created Successfully')
#         print('Account Details')
#         print(f'Account holder Name: {self.name}')
#         print(f'Account Number: {self.account_no}')
#         print(f'Initial Balance: {self.balance}')
#
#     def show_balance(self):
#         print(f'Current balance is {self.balance}')
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Deposit successful new balance is {self.balance}')
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print('Insufficient Balance')
#         else:
#             self.balance -= amount
#             print(f'Withdraw successful new balance is {self.balance}')
#
#
# def find_accounts(acc_no):
#     for acc in accounts:
#         if acc_no == acc.account_no:
#             return acc
#     return None
#
#
# while True:
#     print('----------Bank----------')
#     print('1. Create Account')
#     print('2. Show Balance')
#     print('3. Deposit Money ')
#     print('4. Withdraw Money')
#     print('5. Exit')
#
#     choice = int(input('\nEnter your choice: '))
#
#     match choice:
#         case 1:
#             name = input('Enter your name: ')
#             acc = Bank(name)
#             accounts.append(acc)
#             print(accounts)
#
#         case 2:
#             acc_no = int(input('Enter account no: '))
#             account_details = find_accounts(acc_no)
#             if account_details:
#                 account_details.show_balance()
#             else:
#                 print('Invalid account number')
#
#         case 3:
#             acc_no = int(input('Enter account no: '))
#             account_details = find_accounts(acc_no)
#             if account_details:
#                 amount = int(input('Enter amount to deposit: '))
#                 account_details.deposit(amount)
#             else:
#                 print('Invalid account number')
#
#         case 4:
#             acc_no = int(input('Enter account no: '))
#             account_details = find_accounts(acc_no)
#             if account_details:
#                 amount = int(input('Enter amount to withdraw: '))
#                 account_details.withdraw(amount)
#             else:
#                 print('Invalid account number')
#
#         case 5:
#             break
#
#         case _:
#             print('Invalid choice')


# p7.py
# Detailed inferred question:
# - Build library/book management system with class `Books` and list storage.
# - Book fields: `bookid`, `bookname`, `booktitle`, `bookauthor`, `bookprice`, `bookpage`, `booklang`.
# - Menu:
#   1) Add book
#   2) Show all books
#   3) Show particular book by id
#   4) Update a book
#   5) Delete a book
#   6) Exit

#
# booksDetails = []
#
# class Libray:
#     def __init__(self):
#         self.book_id = int(input('Enter book id: '))
#         self.book_name = input('Enter book Name: ')
#         self.book_author = input('Enter book Author: ')
#         self.book_price = int(input('Enter book Price: '))
#         self.book_pages = int(input('Enter book Pages: '))
#         self.book_language = input('Enter book language: ')
#
#         print('\nBook Added successfully\n')
#
#     def get_books(self):
#             print(f'Book id: {book.book_id}')
#             print(f'Book Name: {book.book_name}')
#             print(f'Book Author: {book.book_author}')
#             print(f'Book Price: {book.book_price}')
#             print(f'Book Pages: {book.book_pages}')
#             print(f'Book language: {book.book_language}')
#
#
#     def update_book(self):
#             book.book_name = input('Enter New book Name: ')
#             book.book_author = input('Enter New book Author: ')
#             book.book_price = int(input('Enter New book Price: '))
#             book.book_pages = int(input('Enter New book Pages: '))
#
#
#     def delete_book(self):
#             booksDetails.remove(book)
#             print('Book Deleted successfully')
#
#
# def find_book(id):
#     for book in booksDetails:
#         if book.book_id == id:
#             return book
#     return None
#
#
# while True:
#     print('\n--------LIBRARY-------')
#     print('1) Add a Book')
#     print('2) Show all books')
#     print('3) Show particular book by id')
#     print('4) Update a book')
#     print('5) Delete a book')
#     print('6) Exit')
#
#     choice = int(input('\nEnter the choice: '))
#
#     match choice:
#         case 1:
#             book = Libray()
#             booksDetails.append(book)
#             print(booksDetails)
#
#         case 2:
#             for book in booksDetails:
#                 book.get_books()
#                 print()
#
#         case 3:
#             id = int(input('Enter book id: '))
#             book = find_book(id)
#             if book:
#                 book.get_books()
#             else:
#                 print('Book not found')
#
#         case 4:
#             id = int(input('Enter book id: '))
#             book = find_book(id)
#             if book:
#                 book.update_book()
#             else:
#                 print('Book not found')
#
#         case 5:
#             id = int(input('Enter book id: '))
#             book = find_book(id)
#             if book:
#                 book.delete_book()
#             else:
#                 print('Book not found')
#
#         case 6:
#             break
#
#         case _:
#             print('invlaid input')
#



# p9.py
# Detailed inferred question:
# - Demonstrate inheritance `Employee(Company)`.
# - Inputs: `companyName`, 'dept', `empName`, `empAge`, `empid`, `empsalary`.
# - Print employee details along with inherited company name and salary.


# class Company:
#     def __init__(self, c, d):
#         self.company_name = c
#         self.department = d
#
# class Employee(Company):
#     def __init__(self):
#         company_name = input('Enter the company name: ')
#         department = input('Enter department name: ')
#         super().__init__(company_name, department)
#         self.emp_name = input('Enter employee Name: ')
#         self.salary = input('Enter salary: ')
#
#     def full_details(self):
#         print(f'Company Name : {self.company_name}')
#         print(f'Department: {self.department}')
#         print(f'Employee name: {self.emp_name}')
#         print(f'Employee age: {self.salary}')
#
# e = Employee()
# e.full_details()


# p10.py
# Detailed inferred question:
# - Demonstrate multiple inheritance `Patient(Hospital, Department)`.
# - Inputs include hospital/department names + patient details:
#   `name`, `age`, `gender`, `admDate`, `bedNo`, optional `dischargeDate`.
# - Print full summary before and after setting discharge date.


# class Hospital:
#     def __init__(self):
#         self.hospital_name = input('Enter hospital Name: ')
#         super().__init__()
#
# class Department:
#     def __init__(self):
#         self.department_name = input('Enter Department Name: ')
#         super().__init__()
#
# class Patients(Hospital, Department):
#     def __init__(self):
#         super().__init__()
#         self.name = input('Enter patient name: ')
#         self.age = int(input('Enter patient age: '))
#         self.gender = input('Enter patient gender: ')
#         self.admDate = input('Enter admission date: ')
#         self.benNo = int(input('Enter bed no: '))
#         self.dischargeDate = None
#
#     def full_summary(self):
#         print(f'Hospital name: {self.hospital_name}')
#         print(f'Department name: {self.department_name}')
#         print(f'Patient name : {self.name}')
#         print(f'Patient age: {self.age}')
#         print(f'Patient gender: {self.gender}')
#         print(f'Patient Admission date : {self.admDate}')
#         print(f'Patient Bed no: {self.benNo}')
#         print(f"Discharge date : {self.dischargeDate if self.dischargeDate else 'Not discharged'}")
#
#     def get_hospital_name(self):
#         print(f'Hospital name: {self.hospital_name}')
#
#     def get_department_name(self):
#         print(f'Department name: {self.department_name}')
#
#     def get_discharge_date(self):
#         print(f'Discharge date: {self.dischargeDate}')
#
#     def set_discharge_date(self):
#         self.dischargeDate = input('Enter discharge date: ')
#
# patient = Patients()
# patient.get_hospital_name()
# patient.get_department_name()
# patient.get_discharge_date()
# patient.full_summary()
# patient.set_discharge_date()
# patient.get_discharge_date()

# p14.py
# Detailed inferred question:
# - Create abstract class `Shape` with abstract methods `area()` and `perimeter()`.
# - Implement subclasses:
#   `Circle` (radius input) and `Rectangle` (length and breadth inputs).

# from abc import ABC, abstractmethod
# from math import  pi
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self):
#         self.radius = int(input('Enter the radius: '))
#
#     def area(self):
#         print(f'Area of circle is {(pi * (self.radius ** 2)):.2f}')
#
#     def perimeter(self):
#         print(f'Perimeter of circle is {(2 * pi * self.radius):.2f}')
#
# class Rectange(Shape):
#     def __init__(self):
#         self.height = int(input('Enter height: '))
#         self.widht = int(input('Enter width: '))
#
#     def area(self):
#         print(f'Area of rectangle is {self.height * self.widht}')
#
#     def perimeter(self):
#         print(f'Area of perimeter is {2 * (self.height + self.widht)}')
#
#
# c = Circle()
# c.area()
# c.perimeter()
# print('\n')
#
# d = Rectange()
# d.area()
# d.perimeter()


# p16.py
# Detailed inferred question:
# - Build abstract employee payroll system with menu:
#   1) Add employee
#   2) Get salary by employee id
# - Base class `Employee`: `empid`, `empname`, `age`, abstract `get_salary()`.
# - Subclasses:
#   `Fixed` -> monthly salary
#   `Hourly` -> `hour * rate`

# from abc import ABC, abstractmethod
#
# employee_details = list()
#
# class Employee(ABC):
#     def __init__(self):
#         self.emp_id = int(input('Enter Employee ID: '))
#         self.emp_name = input('Enter employee name: ')
#         self.age = int(input('Enter Employee age: '))
#
#     @abstractmethod
#     def get_salary(self):
#         pass
#
# class FixedSalary(Employee):
#     def __init__(self):
#         super().__init__()
#         self.salary = float(input('Enter salary: '))
#     def get_salary(self):
#         print(f'Employee salary is : {self.salary}')
#
# class HourlySalary(Employee):
#     def __init__(self):
#         super().__init__()
#         self.hour = int(input('Enter working hour: '))
#         self.rate = float(input('Enter rate per hour: '))
#
#     def get_salary(self):
#         print(f'Employee salary is {self.hour * self.rate}')
#
# def find_employee(id):
#     for emp in employee_details:
#         if emp.emp_id == id:
#             return  emp
#     return None
#
# while True:
#     print('------MENU------')
#     print('1. Add Employee')
#     print('2. Get Salary by ID')
#     print('3. Exit')
#
#     choice = int(input('\nEnter the choice: '))
#
#     match choice:
#         case 1:
#             type = input("Enter Employee type 'F' for Fixed salary, 'H' For Hourly salary: ").upper()
#             match type:
#                 case 'F':
#                     fixed = FixedSalary()
#                     employee_details.append(fixed)
#                 case 'H':
#                     hourly = HourlySalary()
#                     employee_details.append(hourly)
#                 case _:
#                     print('Wrong choice')
#                     continue
#
#         case 2:
#             id = int(input('Enter Employee ID: '))
#             emp = find_employee(id)
#             if emp:
#                 emp.get_salary()
#             else:
#                 print('Wrong ID')
#
#         case 3:
#             break
#
#         case _:
#             print('wrong choice')

# from abc import ABC, abstractmethod
#
#
# class LibraryItem(ABC):
#     auto_id = 1000
#     def __init__(self):
#         self.id = LibraryItem.auto_id
#         self.title = input('Enter title: ')
#         self.author = input('Enter Author name: ')
#         self.is_available = True
#         self.borrow_count = 0
#
#     @abstractmethod
#     def calculate_late_fee(self):
#         pass
#
#     @abstractmethod
#     def get_item_type(self):
#         pass
#
#
#     def borrow_item(self):
#         if self.borrow_count > 0:
#             self.borrow_count -= 1
#             print('Item borrowed\n')
#             if self.borrow_count == 0:
#                 self.is_available = False
#         else:
#             print('Stock empty')
#
#     def return_item(self):
#         if self.borrow_count == 0:
#             self.is_available = True
#
#         self.borrow_count += 1
#         print('Item Returned\n')
#
# class Book(LibraryItem):
#     late_fee_per_day = 2
#
#     def __init__(self):
#         super().__init__()
#         self.page = int(input('Enter page number: '))
#         self.genre = input('Enter genre: ')
#         self.edition = input('Enter edition: ')
#
#     def calculate_late_fee(self):
#         late_days = int(input('Enter late day count: '))
#         return late_days * Book.late_fee_per_day
#
#     def get_item_type(self):
#         return 'Book'
#
# class DVD(LibraryItem):
#     late_fee_per_day = 5
#
#     def __init__(self):
#         super().__init__()
#         self.duration = int(input('Enter duration in minutes: '))
#         self.rating = float(input('Enter rating: '))
#         self.resolution = input('Enter resolution: ')
#
#     def calculate_late_fee(self):
#         late_days = int(input('Enter late day count: '))
#         return late_days * DVD.late_fee_per_day
#
#     def get_item_type(self):
#         return 'DVD'
#






























