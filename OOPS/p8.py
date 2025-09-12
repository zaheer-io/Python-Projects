class parent:
    def m1(self):
        print("Method m1 form class parent")

    def m2(self):
        print("Method m2 form class parent")

class child(parent):
    def m3(self):
        super().m1()
        print("Helllo ")


obj = child()

obj.m3()

