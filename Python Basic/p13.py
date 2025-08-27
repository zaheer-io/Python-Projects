#numeric, text, sequence, mapping, set, boolean, none

num1 = 10 #numeric
num2 = 2.256 #float
num3 = 4 + 5j

t1 = "zaheer" #String

l = [10,20,'hello',2.33] # List
t = (10,'abcd', 1.23) #tuple

dic = {'name' : 'zaheer', 'place' : 'ekm', 'age' : 21} #dictinory

se = {10,'set', 5.3} #set

bo = True
boo = False #boolean

no = None #none

#-----Operator-------

#arithamatic

a = 10
b = 20

print(a + b) #adition

print(a - b) #subtraction

print(a * b) #multliplicaion

print(a / b) #Division

print(a % b) #modulus

print(a // b) #floor division

print(a ** b) #Exponentional


#Relatioanl or comparison

print(a > b) #grether than

print(a < b) #less than

print(a >= b) #grether than or equal to

print(a <= b) #less than or equal to

print(a == b) #comparison


#assignment operator

x = 10 #assignment operator

x+=5 #addition assignment

x-=5 #subtraction assignment

x*=5 #multliplication assignment

x/=5 #divison assignment

x%=10 #modulus assignment

x**=5 #exponentional assignment operator


#Logical operator

y = 20
z = 30

print(y > z and y == z) #and operator

print(y < z or y == z) #or operator

print(not(y > z)) #not operator


#Membership operator

s = 'your name'

print('y' in s) #in operator

print('m' not in s) #not in operator

dic = {'name' : 'zaheer', 'place' : 'ekm', 'age' : 21}

print('zaheer' in dic.values())
print('place' in dic.keys())    #in operator in the case of dictinory


