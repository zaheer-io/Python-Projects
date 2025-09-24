from time import process_time_ns


class MethodOverloading:
    # def show(self):
    #     print("Show first")
    # def show(self, a):
    #     print("Show second", a)

    def show(self, *args):
        print(*args)

    def show(self, **kwargs):
        print(**kwargs)


a = MethodOverloading()

# a.show(50, 60, 70)
# a.show("zaheer" = 10)