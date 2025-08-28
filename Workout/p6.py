
# emp_data = "101,John,HR,35000;102,Ana,IT,55000;103,Sam,Sales,45000"
#
# Output:
#
# {
#  "101": {"name": "John", "dept": "HR", "salary": 35000},
#  "102": {"name": "Ana", "dept": "IT", "salary": 55000},
#  "103": {"name": "Sam", "dept": "Sales", "salary": 45000}
# }

data = "101,John,HR,35000;102,Ana,IT,55000;103,Sam,Sales,45000"

emp_data = data.split(";")
print(emp_data)

d = dict()

for i in emp_data:
    each = i.split(',')

    d[each[0]] = {
            'name' : each[1],
            'dept' : each[2],
            'salary' : each[3]
    }

print(d)