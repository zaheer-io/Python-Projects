#Given a list
fruits=['apple','banana','orange','pineapple','avocado']
#create a new list with elements whose length >5

new = [i for i in fruits if len(i) > 5]
print(new)

##Given a list
l=[12,39,'hello',8.7,-98,-11,5,'python']

#create a new list with only string values

new = [i for i in l if type(i) == str]
print(new)

#create a new list with only positive values
new = [i for i in l if (type(i) == int or type(i) == float) and i > 0]
print(new)

#create a new list with float values
new = [i for i in l if type(i) == float]
print(new)

#create a list with elements whose value is divisible by 3 in the range (1,100)
new = [i for i in l if (type(i) == int and 0 < i < 101) and i % 3 == 0]
print(new)


#Given a string s="python programming'
#create a new list with only vowels

s= "python programming"
new = [i for i in s if i in ['a', 'e', 'i', 'o', 'u']]
print(new)

#given a dictionary d={101:'Arun',102:'Amal',103:'Anu'}
# create a new list with only names
d={101:'Arun',102:'Amal',103:'Anu'}

new = [i for i in d.values()]
print(new)

#given a dictionary d={'a':10,'b':15,'c':20,'d':25}
# create a new list only even values

d={'a':10,'b':15,'c':20,'d':25}

new = [i for i in d.values() if i % 2 == 0]
print(new)
