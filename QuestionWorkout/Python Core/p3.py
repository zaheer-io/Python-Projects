import os

def writefile():
    filename = input("Enter file with extension: ")

    if os.path.exists(filename):
        print("file already exist")
        ch = input("Do you want to over write it? ('y' for yes and 'n' for no: ")
        if ch == 'y':
            content = input("Enter the content: ")
            with open(filename, 'w+') as write:
                write.write(content)
                write.seek(0)
                print("file content is = " + write.read())
        else:
            print("Skip....")
            pass
    print("\n")

def readfile():
    filename = input("Enter file with extension: ")

    if os.path.exists(filename):
        with open(filename, 'r') as read:
            print(read.read())
            print("\n")
    else:
        print("File not found")

    print("\n")

def appendfile():
    filename = input("Enter file with extension: ")
    content = input("Enter the content: ")
    

    print("\n")


def searchfile():
    filename = input("Enter file with extension: ")
    word = input("Enter the word to search: ")

    with open(filename, 'r') as read:
        wordread = read.read()

    if word in wordread:
        print("Word found")
    else:
        print("Word not found")

    print("\n")

def deletefile():
    filename = input("Enter file with extension: ")

    if os.path.exists(filename):
        os.remove(filename)
        print(filename + " Removed successfully")
    else:
        print("File not exist")
    print("\n")

while True:
    print("-----------------------------")
    print("1. Write file                |")
    print("2. Read file                 |")
    print("3. Append file               |")
    print("4. Search a word in a file   |")
    print("5. Delete a file             |")
    print("6. Exit                      |")
    print("------------------------------")

    n = int(input("Enter your choice: "))

    match n:
        case 1:
            writefile()
        case 2:
            readfile()
        case 3:
            appendfile()
        case 4:
            searchfile()
        case 5:
            deletefile()
        case 6:
            print("Existing...")
            exit(0)
