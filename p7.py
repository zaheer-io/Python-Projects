#write a program to swap or interchange two numbers

firstno = int(input("Enter first no: "))
secondno = int(input("Enter second no: "))

print(f"Befor swapping first no is {firstno} and second no is {secondno}")

thirdno = firstno
firstno = secondno
secondno = thirdno

print(f"After swapping first no is {firstno} and second no is {secondno}")

#without using third variable a,b = b,a
firstno,secondno = secondno, firstno

print(f"After swapping without using a third variable first no is {firstno} and second no is {secondno}")