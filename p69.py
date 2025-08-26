

def decateron(division):
    def wrapper(a,b):
        if b == 0:
            return "Cannot divisible by zero"
        else:
            return division(a,b)
    return wrapper


@decateron
def division(a,b):
    return a/b

print(division(20,0))

