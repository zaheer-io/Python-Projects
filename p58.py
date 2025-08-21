#given
l1 = [12,45,67,89,98]
l2 = [34,78,12,56,45]

#find the common elemnts

print(set(l1).intersection(set(l2)))

#find the maximum element from the list

l1 = [12,45,67,89,90]

print(max(l1))

#second  largest element

l1.sort()
print(l1[-2])
print(l1[1])

#find the minimum element form the lsit

print(min(l1))


#find the second smallest element form the list

print(min(l1))

#create a dictinory where keys are numbers and values are count of each numbers

l = [1,1,2,3,3,3,5,6,7,7]

ldict = {i : l.count(i) for i in l}
print(ldict)

#find the maximum salary
d={1:['Arun',23,30000],2:['Amal',26,50000],3:['Anu',24,20000],4:['Kiran',27,60000]}

l3 = [i[2] for i in d.values()]
print(max(l3))

l = [10,5,45,1,85,64]
print(l)

