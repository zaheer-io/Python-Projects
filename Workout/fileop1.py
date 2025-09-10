import os

def ext(filename):
    fullname = ""
    while True:
        print("choose file extension")
        print("1. txt")
        print("2. py")

        ext = int(input("Enter choice: "))

        match ext:
            case 1:
                fullname = filename + ".txt"
            case 2:
                fullname = filename + ".py"
            case _:
                "Choose correct option"
                continue
        break
    return fullname


def writePage():
    filename = input("Enter file name: ")
    fullname = ext(filename)

    if os.path.exists(fullname):
        print("File already exist...")
        choice = input("Do you want to over write it ? ('y' of yes and 'n' for no): ")
        if choice == 'y':
            with open(fullname, 'w+') as write:
                content = input("Enter content: ")
                write.write(content)
                write.seek(0)
                print("Updated data : " + write.read())
                print("\n")
        elif choice == 'n':
            print("skip....")
            print("\n")
            pass
    else:
        print("Creating file" + fullname)
        with open(fullname, 'w+') as write:
            content = input("Enter content: ")
            write.write(content)
            write.seek(0)
            print("Updated data : " + write.read())
            print("\n")

def readPage():
    filename = input("Enter file name: ")
    fullname = ext(filename)

    if os.path.exists(fullname):
        with open(fullname, 'r') as read:
            print(read.read())
            print("\n")
    else:
        print("File not found..")
        print('\n')
        pass

def append():
    filename = input("Enter filename: ")
    fullname = ext(filename)

    if os.path.exists(fullname):
        with open(fullname, 'a+') as appends:
            content = input("Enter content: ")
            appends.write("/n"+content)
            appends.seek(0)
            print("Updated content is: " + appends.read())
    else:
        print("File not found!.")
        print("\n")
        pass

def search():
    filename = input("Enter file name: ")
    fullname = ext(filename)

    if os.path.exists(fullname):
        with open(filename, 'r') as read:
            content = read.read()
            word = input("Enter the word to search: ")

            if word in content:
                print("Word found on the file " + fullname)
            else:
                print("Word not found!.")
        print("\n")
    else:
        print("File not found!. ")
        print("\n")

def apppend():
    filename = input("Enter file name: ")
    fullname = ext(filename)

    if os.path.exists(fullname):
        with open(fullname, 'a+') as append:
            content = input("Enter the content to append: ")
            append.write("\n" + content)
            append.seek(0)
            print("Updated content is:\n" + append.read())
    else:
        print(f"File {fullname} does not exist")


def delete():
    filename = input("Enter file name to delete: ")
    fullname = ext(filename)

    if os.path.exists(fullname):
        print(f"File {fullname} exists..")
        ch = input("Do you want to delete the file ? ('y' for yes and 'n' for no) ")
        if ch == 'y':
            os.remove(fullname)
        elif ch == 'n':
            pass
        else:
            print("Enter valid choice !")
            pass
    else:
        print(f"File {fullname} not found !")
        pass

apppend()





