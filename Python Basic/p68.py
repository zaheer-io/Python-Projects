#
# def change(fun):
#     def innter(a,b):
#         if a < b:
#             a,b = b,a
#         return fun(a, b)
#     return innter
#
# @change
# def sub(a,b):
#     return a - b
#
# print(sub(30,5))



def decattor(swap):
    def wraper(a,b):
        if b > a:
            a,b = b,a
        return swap(a,b)
    return wraper

@decattor
def sub(a,b):
    return a-b

print(sub(10,15))


print