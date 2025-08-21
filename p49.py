#given a list create a new list with first letter form each word

# l = ['apple', 'orange', 'pineapple']
#
#
# new = [i[0] for i in l]
#
# print(new)


#given a list create with new list even values,
# create a new list with odd values
#create a new list with numbers less than 50

l= [12, 75, 67, 13, 56, 11]

neweven = [i for i in l if i % 2 == 0]

newodd = [i for i in l if i % 2 != 0]

larnum = [i for i in l if i < 50]

print(neweven,"\n",newodd,"\n",larnum, end=" ")


