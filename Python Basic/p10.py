"""

write a python program
1. print the given string
2. print the reverse of the string
3. print the length of the string
4. print the 7th character of the string
5. print the 13th index of the string
6. print the character from 4 index to 12 index position
7. print the last character
8. revomves the character from 0th index to 5 th index positon adn print the remaining string

"""


s = "Pthon is a programming language"

print(f"String = {s}")
print("\n")

print(f"reverse of the string = {s[::-1]}")
print("\n")

print(f"Length of the string = {len(s)}")
print("\n")

print(f"7 th character of the string = {s[6]}")
print("\n")

print(f"13 index of the string = {s[13]}")
print("\n")

print(f"Character from 4th index to 12th index = {s[4:13]}")
print("\n")

print(f"Last character of the string = {s[-1]}")
print("\n\n\n")


t = "Hello world"
g = t[6:]
print(f"Remaining index position = {g}")
print("\n\n\n")


# new = "Hello world"
# new[4] = "k"
# print(new)
