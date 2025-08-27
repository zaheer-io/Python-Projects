#WAP to check whether a given year is a leap year or not.
"""

leap = int(input("Enter year: "))

if leap % 4 == 0:
    print("Leap year")
else:
    print("not a leap year")



#WAP to find prime nos

pn = int(input("Enter a number: "))
i = 2
p = 0
while i < pn:
    if pn % i == 0:
        p = 1;
        break
    i+=1

if p == 0:
    print("Prime no")
else:
    print("not a prime no")



#WAP to print all prime numbers between 1 and 100.
p = 0
for i in range(2,101):

    for j in range(2,i):
        if i % j == 0:
            p = 1
            break

    if p == 0:
        print(i)
    p = 0



#WAP to print the multiplication table of a number.

mn = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{i} x {mn} = {i * mn}")




#WAP to print the factorial of a number.

fn = int(input("Enter a number: "))
fact = 1
for i in range (1, fn):
    fact += fact * i
print(fact)


#WAP to count the number of digits in a given number.

cn = int(input("Enter a number: "))
ln = 1
for i in range (1, cn):

    cn = cn // 10
    if cn == 0:
        break

    ln+=1

print(ln)



#WAP to reverse a number and check if it's a palindrome.

n = int(input("Enter a number: "))
rev = 0
while n > 0:
    a = n % 10
    rev = (rev * 10) + a
    n = n // 10

print(rev)

"""


#WAP to count vowels, consonants, digits, and spaces in a sentence.

sen = input("Enter a sentence: ")

listsen = list(sen)

print(listsen)

lengthlist = len(listsen)
print(lengthlist)

nolist = [1,2,3,4,5,6,7,8,9,0]
volist = ['a', 'e', 'i', 'o', 'u']

print(listsen[0])
nos=vow=spc=con=0
newvowel = newno = newcon = []

for i in range (0, lengthlist):
    if listsen[i] in nolist:
        nos +=1
        newvowel.append(listsen[i])
    elif listsen[i] in volist:
        vow +=1
    elif listsen[i] == ' ':
        spc +=1
    else:
        con +=1

print(f" nos {nos}, vowels {vow}, space {spc} and consonent {con}")

print(newvowel)