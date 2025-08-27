#create a list of 5 food items
#Add a new food item to the list
#update the second food item
#update the second food item to new value
#print the updated list
#print the length of the list
#print the reverse of the list
#print the last food item
#5print the 5th food item

food = ["porota", "chappthi", "laddu", "gilebi", "peda"]

print(f"food item = {food}")

food.append("Kulfi")
print(f"updated food item = {food}")

food[1] = "Banana"
print(f"updated food item = {food}")

print(f"length of the list {len(food)}")

print(f"Reverse of the list {food[::-1]}")

print(f"Last food item {food[-1]}")

print(f"5th food item {food[4]}")

#question 2

l = [23,56,89,10,67,45,17]
print(f"Before interchange list {l}")

l[1],l[5] = l[5],l[1]
print(f"After Interchange new list {l}")