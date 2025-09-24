#Abstract class

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def periemter(self):
        pass

class Circle(Shape):

    def __init__(self):
        self.r = int(input("Enter the radius: "))

    def area(self):
        print(f"Area of Circle is {3.14 * self.r ** 2}")

    def periemter(self):
        print(f"Perimeter of the circle is {2 * 3.14 * self.r}")

class Rectange (Shape):
    def __init__(self):
        self.l = int(input("Enter the length: "))
        self.b = int(input("Enter the bredth: "))

    def area(self):
        print(f"Area of the Rectange is {self.l * self.b}")

    def periemter(self):
        print(f"Perimeter of the Rectange is {2 * self.l * self.b}")

c = Circle()
c.area()
c.periemter()

print("\n")

r = Rectange()
r.area()
r.periemter()