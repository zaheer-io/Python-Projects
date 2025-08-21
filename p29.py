import time

name = input("Enter your name: ") #hello world

namelist = []

for k in name:
    namelist.append(k.lower())

skip = [91,92,93,94,95,96]

for i in namelist:
    for a in range(97, ord(i)):
        print(chr(a), end="", flush=True)
        time.sleep(.05)
        print("\r", end="", flush=True)

    print(i, end="", flush=True)


