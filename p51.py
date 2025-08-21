l = [1,2,3,4]
new = {i : i **2 for i in l}
print(new)

#given a string s = "python is a programming language" create a dictionary where keys are words adn values are lenght of each word
s = "python is a programming language"
news = s.split()
print(news)

new = {i : len(i) for i in news}
print(new)

#create a list with no duplicates l = [1,1,2,3,4,5,6,6,7,7]
l = [1,1,2,3,4,5,6,6,7,7]
seem = []

new = [i for i in l if(i not in seem)]
print(new)
print(seem)

#create a list l = [10, 20, 30, 40]

