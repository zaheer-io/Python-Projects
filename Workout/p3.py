# Input student names and marks (comma-separated).
# Build a dictionary:
from selectors import SelectSelector

# {name: {"marks": score, "grade": "A/B/C/F", "pass": True/False}}

namesmarks = input("Enter the student names and mark (comma seperated): ")
namemarklist = namesmarks.split(",")
print(namemarklist)

def grade(n):
    mark = int(n)

    match mark:
        case m if 80 < m <= 100:
            return "A"
        case m if 60 < m <= 80:
            return "B"
        case m if 40 < m <= 60:
            return "C"
        case m if 20 < m <= 40:
            return "D"
        case m if 0 <= m <= 20:
            return "F"
        case _:
            return "Invalid"

d = dict()

d[namemarklist[0]] = {
    'marks' : namemarklist[1],
    'Grade' : grade(namemarklist[1])
}

print(d)