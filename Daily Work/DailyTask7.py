#pattern

# for i in range(1, 8):
#     print("1" * i)
#     if i % 2 == 0:
#         print()

for i in range(1, 8):
    for j in range(1, i + 1):
        if i % 2 != 0:
            if j % 2 != 0:
                print(1, end=" ")
            else:
                print(0,end=" ")
        else:
            if j % 2 != 0:
                print(0, end=" ")
            else:
                print(1,end=" ")
    print()