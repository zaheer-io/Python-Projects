class Person:
    def __init__(self): #Self represents current object constructior method to create and initialise objects of a class
        self.name = input("Enter name")
        self.age = input("Enter age")

    def show(self):
        print(self.name, self.age)

#Object creation

p1 = Person()

p1.show()
