# For numbers 1–20, build a dictionary:
#
# {n: {"prime": True/False, "factors": [list_of_factors]}}

d = dict()

for n in range(1, 21):
    d[n] = {
        'prime' : "True" if n > 1 and all(n % i != 0 for i in range(2, n-1)) else "False",
        'Factors' : [i for i in range(1, n+1) if n % i == 0]
    }

print(d)