# students = [{"id":1,"name":"John"},{"id":2,"name":"Ana"}]
# Convert into:
#
# python
# Copy code
# {1: "John", 2: "Ana"}

students = [{"id":1,"name":"John"},{"id":2,"name":"Ana"}]

d = {i['id'] : i['name'] for i in students}
print(d)