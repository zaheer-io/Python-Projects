# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

print("\n\n")

for i in range(1, 6):
    print("* " * i, end=" ")
    print()

#     *
#    **
#   ***
#  ****
# *****

for i in range(5, 0, -1):
    print("  " * (i-1), end=" ")
    print("* " * (6 - i)) # ((n + 1) - i - 1) % 5) + 1


print("\n\n")

# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n\n")

# *****
# ****
# ***
# **
# *

for i in range(5, 0, -1):
    print("* " * i, end=" ")
    print()


print("\n\n")

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


k = 6
for i in range(1, 5):
    for k in range(1, k + 1):
        print(end=" ")
    k-= 2
    for j in range(1, i + 1):
        print("  * ", end="")
    print()


k = 0
for i in range(4, 0, -1):
    for k in range(1, k + 1):
        print(end=" ")
    k += 2
    for j in range(1, i + 1):
        print("  * ", end="")
    print()







