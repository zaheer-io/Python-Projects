# Take a sentence.
# Output a dict where key = word length, value = list of words of that length.

s = input("Enter the sentence: ")

words = s.split()
d = dict()

for i in words:
    d[len(i)] = [word for word in words if len(i) == len(word)]

print(d)