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

#find the minimum element form the lsit

print(min(l1))


#find the second smallest element form the list

l1.sort(reverse=True)
print(l1[-2])

#create a dictinory where keys are numbers and values are count of each numbers

l1 = [12,45,67,89,7790]

l = {i : len(str(i)) for i in l1}
print(l)


#find the maximum salary
d={1:['Arun',23,30000],2:['Amal',26,50000],3:['Anu',24,20000],4:['Kiran',27,60000]}

print(max([i[2] for i in d.values()]))
