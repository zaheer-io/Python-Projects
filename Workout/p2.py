s = input("Enter the string: ")

slist = list(s.replace(" ",""))
print(slist)

d = dict()

for i in slist:
    d[i] = {
        'count' : slist.count(i),
        'is_vowel' : i in ['a','e','i','o','u'],
        'ascci' : ord(i)
    }
print(d)






# newslist = [i for i in s if i != ' ']
# print(newslist)