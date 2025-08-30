# keys = ["a", "b", "c"]
# values = [10, 20, 30]
# Create a dict and also make reverse mapping in another dict.

keys = ["a", "b", "c"]
values = [10, 20, 30]

d = dict()

for k, y in zip(keys, values):
    d[k] = y

print(d)