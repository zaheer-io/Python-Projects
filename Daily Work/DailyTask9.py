digitList = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

n = int(input("Enter a number: "))

numlist = list(map(int, str(n)))

numDict = dict()

for num in numlist:
    numDict[num] = digitList[num]

print(numDict)