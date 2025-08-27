students = [
    {'id': 1, 'name': 'Asha', 'marks': [98, 82, 91, 97, 89]},
    {'id': 2, 'name': 'John', 'marks': [88, 76, 92, 85, 77]},
    {'id': 3, 'name': 'Maya', 'marks': [70, 70, 84, 79, 88]},
]

# (a) Print each student’s name and average marks.
#
# (b) Identify and print the topper (highest average).
#
# (c) List all students who scored above 80 in at least 3 subjects.
#
# (d) Create a dictionary mapping student id to grade:
#
# A (avg ≥ 90), B (80–89), C (70–79), D (<70)

# highavg = {}
# high = 0.00
#
# for i in students:
#     print(i["name"], end=" Has average mark of ")
#     avg = 0
#     sum = 0
#     for j in i["marks"]:
#         sum = sum + j
#         avg = sum / len(i["marks"])
#         if avg > high:
#             highavg = dict(name = i['name'], averagemark = avg)
#             high = avg
#     print(avg)
#     avg = 0
#
# print("\n")
# print(f"highest average is ({highavg['name']}) = {highavg['averagemark']}")


# for i in students:
#     std = i['name']
#     mark = []
#     total = 0
#     for j in i['marks']:
#         if j > 80:
#             mark.append(j)
#             total += 1
#     if total >= 3:
#         print("Student who scored more than 80 in atleast 3 sub is ", std, " ", mark)

# A (avg ≥ 90), B (80–89), C (70–79), D (<70)

dictcopy = students.copy()

for i in dictcopy:
    sum = avg = 0
    grade = ""
    for j in i['marks']:
        sum += j
    avg = sum / len(i['marks'])

    if avg >= 90: grade = 'A'
    elif avg >= 80: grade = 'B'
    elif avg >= 70: grade = 'C'
    elif avg < 70: grade = 'D'

    i['avg'] = avg
    i['grade'] = grade
    print(i)

print(students)








