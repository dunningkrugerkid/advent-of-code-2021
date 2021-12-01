# part one
fileIn = open("aoc1input.txt","r")
listOfDepths = [eval(x) for x in fileIn]
fileIn.close()
largerTotal = 0
increment = 0
for depth in listOfDepths:
    if depth == listOfDepths[-1]:
        break
    elif listOfDepths[increment+1] > listOfDepths[increment]:
        largerTotal += 1
    increment += 1
print("total: ", largerTotal)