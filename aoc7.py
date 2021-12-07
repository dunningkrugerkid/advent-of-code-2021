input = open("aoc7input.txt","r")

inputListStrings = input.read().split(",")
finalInputList = [int(x) for x in inputListStrings]

minCrabPos = min(finalInputList)
maxCrabPos = max(finalInputList)

fuelTotals = []

for x in range(minCrabPos,maxCrabPos):
    cost = 0
    for n in finalInputList:
        dist = abs(n - x)
        cost += (((dist**2)+dist)/2)
    fuelTotals.append(cost)

print(min(fuelTotals))