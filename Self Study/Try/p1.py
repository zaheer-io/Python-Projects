import copy

l1 = [1, 2, 3, [4, 5]]
l2 = copy.copy(l1)
l3 = copy.deepcopy(l1)

print(l1)
print(l2)

# l2[3][1] = 2

#
# print('before shallow copy')
#
# print(l1)
# print(l2)

l3[3][1] = 6
print('before deep copy')

print(l1)
print(l3)