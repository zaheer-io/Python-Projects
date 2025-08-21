#wap to check whether a number is 2 digit , 3 digit and 4 digit number

"""

"""


num1 = int(input("Enter a 2 digit, 3 digit or 4 digit number: "))
num1str = str(num1)

if len(num1str) == 2:
    print(f"{num1} is a 2 digit number")
elif len(num1str) == 3:
    print(f"{num1} is a 3 digit number")
elif len(num1str) == 4:
    print(f"{num1} is a 4 digit number")
else:
    print("Read question first!!!")





#wap to perform arithmetic operator
print("\n\n")

num3 = int(input("Enter first number: "))
num4 = int(input("Enter second nubmer: "))
opn = input("+ for additon, - for subtraction , * for multiplication and / for division: ")

if opn == "+":
    print("additon = ",num3 + num4)
elif opn == "-":
    print("subtraction = ",num3 - num4)
elif opn == "*":
    print("Multliplication = ",num3 * num4)
elif opn == "/":
    print("Division = ", num3 / num4)
else:
    print("invalid operator")


#wap to point the grade of a student
print("\n\n")

score = int(input("Enter grade of the student: "))

if score >= 91 and score <=100:
    print("Grade A")
elif score >=81 and score <=90:
    print("Grade B")
elif score >=71 and score <= 80:
    print("Grade C")
elif score >=61 and score <= 70:
    print("Grade D")
elif score < 61 and score >=0:
    print("E")
else:
    print("seriously!")



#wap to print the triangle is isosceles,equilateral or scalene
print("\n\n")



sideA = int(input("Enter first side: "))
sideB = int(input("Enter second side: "))
sideC = int(input("Enter third side: "))

if sideA == sideB or sideB == sideC or sideC == sideA:
    print("Isoscels triangle")
elif sideA == sideB == sideC:
    print("Equilateral Triangle")
else:
    print("Scalene triangle")



#wap to print number of days in a month
print("\n\n")


month = input("Enter month name: ")

month1 = ["january", 'march', "may" , "july" , "august", "october", 'december'] #January, March, May, July, August, October, and December
month2 = ["april", 'june', "september", "november"]

if month in month1:
    print("number of days is 31")
elif month in month2:
    print("number of days is 30")
elif month == 'february':
    print("number of days is 28")
else:
    print("Check spelling!!")



month = input("Enter month name: ")

dicti1 = {'january' : 31, 'february' : 28, 'march' : 31, 'april' : 30}

if month in dicti1.keys():
    print(dicti1[month])
