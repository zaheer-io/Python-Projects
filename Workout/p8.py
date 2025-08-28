# 7. Dictionary of Squares and Cubes
#
# Given a list of numbers, create:
#
# {num: {"square": num**2, "cube": num**3, "even": True/False}}

n = input("Enter the numbers (devide by comma): ")

numlist = list(map(int, str(n).split(',')))
print(numlist)

d = dict()

