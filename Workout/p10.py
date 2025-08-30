# 10. Dictionary Sorting

# Given a dictionary of names and marks,
# sort by:
#
# Keys (alphabetical)
#
# Values (descending order)

d = {'zaheer' : 50, 'anjana' : 85, 'archana' : 62, 'appus' : 49, 'rahim' : 69}

print(dict(sorted(d.items()))) #sorted by keys ascending order
print(dict(sorted(d.items(), key=lambda x : x[1]))) #sorted by values ascending order

print(dict(sorted(d.items(), key= lambda x : x[0], reverse=True))) #Sorted by keys descending order
print(dict(sorted(d.items(), reverse=True))) #sorted by keys descending order #Works fine don't a effcient method 
print(dict(sorted(d.items(), key= lambda x : x[1], reverse=True))) #sorted by values descending order