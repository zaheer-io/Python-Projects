bookslist = list()

class Books:
    def __init__(self, bookname):
        self.bookid = int(input("Enter book id: "))
        self.bookname = bookname
        self.booktitle = input("Enter book title: ")
        self.bookauthor = input("Enter book author name: ")
        self.bookprice = int(input("Enter book price: "))
        self.bookpage = int(input("Enter book page no: "))
        self.booklang = input("Enter book language: ")
        print("Book added \n")

    def showbook(self):
        print(f"Details of book {self.bookname}")
        print(f"Book id {self.bookid}")
        print(f"Book title {self.booktitle}")
        print(f"Author name {self.bookauthor}")
        print(f"No of pages {self.bookpage}")
        print(f"Book language {self.booklang}")
        print("\n")


    def updateBooke(self):

        bookid = int(input("Enter book id : "))
        book = find_book(bookid)

        if book:
            print("which details to update: ")
            print(f"2. Book title: ")
            print(f"3. Author name: ")
            print(f"4. No of pages: ")
            print(f"5. Book language: ")

            choice = int(input("Enter the choice:"))

            match choice:
                case 1:
                    title = input("Enter new title: ")
                    self.booktitle = title

                case 2:
                    author = input("Enter new author namef: ")
                    self.bookauthor = author

                case 3:
                    pages = int(input("Enter page number: "))
                    self.bookpage = pages

                case 4:
                    lang = input("Enter book language: ")
                    self.booklang = lang

                case _:
                    print("Invlaid entry")

    def deletebook(self):
        bookslist.remove(self)
        print("Book removed")


def find_book(bookid):
    for i in bookslist:
        if i.bookid == bookid:
            return i
    return None

while True:
    print("Library operations: ")
    print("1. Add a book")
    print("2. Show all book: ")
    print("3. show particular book: ")
    print("4. Update a book: ")
    print("5. Delete a book: ")
    print("6. Exit")

    choice = int(input("Enter the choice: "))

    match choice:
        case 1:
            name = input("Enter book name: ")
            book = Books(name)
            bookslist.append(book)

        case 2:
            for i in bookslist:
                i.showbook()

        case 3:
            bookno = int(input("Enter book id: "))
            book = find_book(bookno)

            if book:
                book.showbook()
            else:
                print("Book not found")

        case 4:
            bookno = int(input("Enter book id: "))
            book = find_book(bookno)

            if book:
                book.updateBooke()

        case 5:
            bookno = int(input("Enter book id: "))
            book = find_book(bookno)

            if book:
                book.deletebook()
            else:
                print("Book not found")

        case 6:
            exit()

        case _:
            print("Enter valid choice")