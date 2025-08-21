# n = int(input("Enter a number: "))
#
# i = 1
# fact = 1
#
# while i <= n:
#     fact = fact * i
#     i += 1
#
# print("Factorial is ", fact)
#
#
# #Multliplicatio table of a numnber
#
#
# mul = int(input("Enter a number: "))
# i = 1
#
# while i <= 10:
#     print(i, " x ", mul, " = ", (mul * i))
#     i +=1


n = int(input("Enter a number: "))
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1
