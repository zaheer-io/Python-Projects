# Given a list of tuples:
#
# [("apple", 3), ("banana", 5), ("apple", 2), ("orange", 1)]
#
# Convert into:
#
# {"apple": {"count": 5}, "banana": {"count": 5}, "orange": {"count": 1}}



sample = [("apple", 3), ("banana", 5), ("apple", 2), ("orange", 1)]

d = dict()


for i in sample:
    d[i[0]]= {
        'count' : i[1]
    }
print(d)