# Write a program to read a sentence and build a dictionary:
#
# {word : {"length": len(word), "vowels": number_of_vowels, "is_palindrome": True/False}}


s = input("Enter the string: ")

d = {}
words = s.split()

vowels = ['a', 'e', 'i', 'o', 'u']

for i in words:
    d.update({
        i : {'length' : len(i), 'count' : s.count(i), 'is_palinrome' : i == i[::-1], 'number_of_vowesl' : len(list(filter(lambda x : x in vowels, i))), 'number_of_consonent' : len(list(filter(lambda x : x not in vowels, i)))}
    })

print(d)
