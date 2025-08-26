# for i in range(1, 5):
#     print(1)
#
# for i in range(1, 5):
#     for j in range(1, i  + 1):
#         if j % 2 == 0: print(2, end=" ")
#         else: print(1, end=" ")
#     print()
#
# print("\n")
#
# for i in range(1, 5+1):
#     for j in range(1, 5+1):
#         if i == j: print(i, end=" ")
#         else: print(0, end=" ")
#     print()
#
#
# print("\n")
#
#
# k = 1
# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(k, end=" ")
#         k+=1
#     print()
#
#
# print("\n")
#
# k = 65
#
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(chr(k), end=" ")
#     print()
#     k += 1
#
# print("\n")
#
#
# for i in range(1, 5):
#     k = 65
#     for j in range(1, i + 1):
#         print(chr(k), end=" ")
#         k +=1
#     print()
#
# k = 6
# for i in range(1, 5):
#     for k in range(1, k + 1):
#         print(end=" ")
#     k-= 2
#     for j in range(1, i + 1):
#         print("* ", end="")
#     print()
#
# print("\n")
#
# # for i in range(1, 6):
# #     print("  " * ((6 - i - 1) % 5), end=" ")
# #     print(" *  " * i, end=" ")
# #     print()
# #
# # print("\n")
#
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
#
# for i in range(6, 0, -1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
#
#
#
#
#
#
#
# print("\n")
#
# k = 6
# for i in range(1, 5):
#     for k in range(-1, k + 1):
#         print(end=" ")
#     k-= 2
#     for j in range(1, i + 1):
#         print("* ", end="")
#     print()
#
# k = 0
# for i in range(5, 0, -1):
#     for p in range(1, k+1):
#         print(end=" ")
#     k += 2
#
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
#
# print("\n")
#
#
#
# k = 6
# for i in range(1, 5):
#     for k in range(1, k + 1):
#         print(end=" ")
#     k-= 2
#     for j in range(1, i + 1):
#         print("*", end="   ")
#     print()
#
# k = 0
# for i in range(4, 0, -1):
#     for k in range(1, k + 1):
#         print(end=" ")
#     k += 2
#     for j in range(1, i + 1):
#         print("*", end="   ")
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#
#

# size = 6
# for i in range(size + 1):
#     print("* " *  (i + 1),)
# for i in range(size):
#     count = size - i
#     print("* " * count)


#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

size = 6

for i in range(size):
    space = size - (i + 1)
    print(" " * space, end=" ")
    print("*" * i)

#
#
#       *
#     *   *
#   *   *   *
# *   *   *   *
# *   *   *   *
#   *   *   *
#     *   *
#       *
