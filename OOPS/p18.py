# 1. Library Management System (Abstract + Polymorphism + List of Objects)
#
# Design an OOP system for a library:
#
# LibraryItem → abstract base class with common attributes: title, author, id.
#
# Two subclasses:
#
# Book (with extra attr: pages)
#
# DVD (with extra attr: duration)
#
# LibraryItem should have an abstract method get_details() implemented differently in subclasses.
#
# Store multiple items in a list. Print details polymorphically.
#
# Add a method borrow_item() and return_item() which updates availability.
#
# 👉 Question: How will you manage borrowing/returning in both subclasses without writing duplicate code?

from abc import ABC, abstractmethod
from time import process_time_ns

items = list()

class LibraryItem(ABC):
    def __init__(self):
        self.id = int(input("Enter the ID: "))
        self.title = input("Enter the Title: ")
        self.author = input("Enter the Author: ")

    @abstractmethod
    def borrow_item(self):
        pass

    def return_item(self):
        pass

class Book(LibraryItem):
    def __init__(self):
        LibraryItem.__init__(self)
        self.pages = int(input("Enter the Page Number:"))
        self.itemAvailable = True

    def borrow_item(self):
        print(f"Book Borrowed : {self.id}, {self.title}")
        self.itemAvailable = False

    def return_item(self):
        print(f"Book returned: {self.id}, {self.title}")
        self.itemAvailable = True

    def view_books(self):
        print(f"Book id : {self.id}")
        print(f"Book title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Book pages : {self.pages}")


class DVD(LibraryItem):
    def __init__(self):
        LibraryItem.__init__(self)
        self.duration = int(input("Enter Duration in Miniuts:"))
        self.itemAvailable = True

    def borrow_item(self):
        print(f"DVD Borrowed : {self.id}, {self.title}")
        self.itemAvailable = False

    def return_item(self):
        print(f"DVD returned: {self.id}, {self.title}")
        self.itemAvailable = True

    def view_dvd(self):
        print(f"DVD id : {self.id}")
        print(f"DVD title: {self.title}")
        print(f"DVD Author: {self.author}")
        print(f"DVD Duration : {self.duration}")

def find_item(item_id):
    for objs in items:
        if objs.id == item_id:
            return objs
    return None

while True:
    print("Library Management Systems")
    print("1. Add item (for admin)") #adin pass = 226027
    print("2. View all Items: ")
    print("3. Borrow a Item")
    print("4. Return Item")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            password = int(input("Enter admin password: "))
            if password == 226027:
                item_type = input("Enter the type ('b' for Book's and 'd' for DVD's : ")
                if item_type == 'b':
                    book_obj = Book()
                    items.append(book_obj)
                    print("Book Added ....")
                elif item_type == 'd':
                    dvd_obj = DVD()
                    items.append(dvd_obj)
                    print("DVD Added ....")
                else:
                    print("Enter correct option!")
                    pass
            else:
                print("Password is wrong")

            print(items)
            print("\n")


        case 2:
            item_type = input("Enter the type ('b' for Book's and 'd' for DVD's : ")

            if item_type == 'b':
                for obj in items:
                    if hasattr(obj, "pages"):
                        if obj.itemAvailable:
                            obj.view_books()
                            print("\n")
            elif item_type == 'd':
                for obj in items:
                    if hasattr(obj, "duration"):
                        if obj.itemAvailable:
                            obj.view_dvd()
                            print("\n")
            else:
                print("Enter correct option!")
                pass

        case 3:
            item_type = input("Enter the type ('b' for Book's and 'd' for DVD's : ")

            if item_type == 'b':
                b_id = int(input("Enter Book ID: "))
                obj = find_item(b_id)
                if obj:
                    obj.borrow_item()
                    print("Book Borrowed")
                else:
                    print("Item not found")
            elif item_type == 'd':
                d_id = int(input("Enter DVD ID: "))
                obj = find_item(d_id)
                if obj:
                    obj.borrow_item()
                    print("DVD Borrowed")
                else:
                    print("Item not found")

            print("\n")

        case 4:
            item_type = input("Enter the type ('b' for Book's and 'd' for DVD's : ")

            if item_type == 'b':
                b_id = int(input("Enter Book ID: "))
                obj = find_item(b_id)
                if obj:
                    obj.return_item()
                    print("Book Returned")
                else:
                    print("Item not found")
            elif item_type == 'd':
                d_id = int(input("Enter DVD ID: "))
                obj = find_item(d_id)
                if obj:
                    obj.return_item()
                    print("DVD Returned")
                else:
                    print("Item not found")