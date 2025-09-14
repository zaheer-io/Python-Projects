# 1
# 22
# *
# 4444
# 55555

for i in range(1, 7):
    if i % 3 == 0:
        print("*" * i)
        continue
    for j in range(1, i+1):
        print(i, end=" ")
    print("\n")