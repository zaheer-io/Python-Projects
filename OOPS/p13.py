#Dender methods

class A:
    def __init__(self):
        self.x = int(input("Enter a number: "))

    def __add__(self, other, oth):
        return self.x + other.x + oth.x

a = A()
b = A()
c = A()

print(a + b)
print(a)