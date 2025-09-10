#Define a class named book with attributes bookid, title, author, page, price, language and methods

#getauthor, getprice, getittile , setatuthor, setprice, settitile

class Books:
    def __init__(self):
        self.bookid = int(input("Enter the book id: "))
        self.title = input("Enter title name: ")
        self.author = input("Enter author name: ")
        self.page = int(input("Enter the page number: "))
        self.price = int(input("Enter book price: "))
        self.language = input("Enter the language: ")

    def getauthor(self):
        print(f"Author name: {self.author}")

    def gettitle(self):
        print(f"Title name: {self.title}")

    def getprice(self):
        print(f"Price : {self.price}")

    def setatuthor(self):
        temp  = self.author
        self.author = input("Enter new author name: ")
        print(f"Author named change to '{temp}' to '{self.author}'")

    def settitle(self):
        temp = self.title
        self.title = input("Enter new title: ")
        print(f"Title change to '{temp}' to '{self.title}'")

    def setprice(self):
        temp = self.price
        self.price = int(input("Enter new price: "))
        print(f"Price change to '{temp}' to '{self.price}'")


b1 = Books()

print("\n")

b1.getauthor()
b1.gettitle()
b1.getprice()

print("\n")

b1.setatuthor()
b1.settitle()
b1.setprice()

b2 = Books()

print("\n")

b2.getauthor()
b2.gettitle()
b2.getprice()

print("\n")

b2.setatuthor()
b2.settitle()
b2.setprice()


