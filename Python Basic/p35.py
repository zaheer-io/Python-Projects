s = "python is a programming language"
vow = ['a', 'e', 'i', 'o', 'u', " "]

for i in s.lower():
    if i in vow:
        continue
    print(i)


print("\n\n")
l = [23,56, 89, 12, 90, 13, 60]

for no in l:
    if no > 15:
        print(no)



print("\n\n")

col = ['red', 'green', 'orange', 'yello', 'blue']

for colour in col:
    if len(colour) > 5:
        print(colour)

print("\n\n")
d = {'country1' : 'India', 'country2' : 'nepal', 'country3' : 'newzland', 'country4' : 'iceland'}

for country in d.values():
    if country.__contains__("land"): # if 'land' in country: --> print(country)
        print(country)


print("\n\n")
li = ['arun', 34, 'hello', 9.8]

for st in li:
    if type(st) == str:
        print(st)