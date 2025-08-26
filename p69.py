

def decerator(division):
    def inner(a, b):
        if b != 0:
            return division(a,b)
        else:
            return "Error"
    return inner


@decerator
def division(a,b):
    return a / b


print(division(10,5))

