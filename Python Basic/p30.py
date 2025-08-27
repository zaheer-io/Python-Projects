"""

from itertools import count

# i = 200
#
# while i <= 400:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1


#count of those numbers that are divisible 3 and 5 in the range 200 to 400

j = 200
count = 0

while j <= 400:
    if j % 3 == 0 and j % 5 == 0:
        count +=1
    j +=1

print(count)

#wap count of those numbers that are divisible by 7 in the range 1500 to 2700

k  = 1500
count1 = 0

while k <= 2700:
    if k % 7 == 0:
        count1 +=1
    k +=1

print(count1)


# sum of first 5 numbes

s = 1
c = 0

while s <= 5:
    c += s
    s += 1

print(c)



p = 1

d = 1

while p <= 5:
    d *= p
    p += 1
print(d)

"""

#sum of numbers from 200 to 400

i = 200
s = 0

while i <= 400:
    s += i
    i += 1

print("Sum of no from 200 to 400 = ",s)


#sum of square of numbers from 1 to 10

j = 1
s1 = 1

while j <= 10:
    s1 = s1 + (j ** 2)
    j += 1

print("Sum of square of 1 to 10 = ", s1)

#sum of product of numbers from 1 to 10

k = 1
p = 1

while k <= 10:
    p = p * k
    k += 1

print("Product of numbers from 0 to 10 = ", p)

#product of even numbers from 1 to 100

l = 1
e = 1

while l <= 100:
    if l % 2 == 0:
        e *= l
    l +=1

print("Producto of even numbers from 1 to 200 = ", e)

#sum and count of numbers that are divisible by 3 in the range 1 to 50

m = 1
di = 0
dk = 0

while m <= 50:
    if m % 3 == 0:
        di += m
        dk +=1
    m +=1

print("sum of 1 to 50 divisible by 3 = ", di)
print("Count of 1 to 50  divisible by 3= ", dk)




