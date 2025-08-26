# #global scope
#
# x = 20
#
# def msg():
#     print(x)
#     global x
#     x = 30
#
#
# msg()
#
#
# # print(x)
# #
# # def new_msg():
# #     y = 30
# #     print("hello ", y)
#
#
# # new_msg()
# #print(y)

# def outer():
#     x = 10 #enlosing variable
#     print(x)
#     print(y)
#     def inner():
#         nonlocal x
#         global y
#         x = 10
#         y = 20
#         print(x)
#     inner()
#
# outer()


def outer():
    x = 10
    print(f"outer {x}")
    def inner():
        y = 10
        print(f"inner {y}")
        def ininner():
            z = 20
            print(f"ininner {z}")
            print(f"access innter {y}")
            print(f"access outer {x}")
        ininner()
    inner()
outer()

