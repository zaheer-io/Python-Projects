s = "python is a programming language"

ch = input('Enter a character: ')

ind = (s.index(ch) + 1)
#print(ind)

ch = s[ind]
print(ch)

for i  in s:
    if i == ch:
        break
    print(i, end="")