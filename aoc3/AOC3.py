# part one
fileIn = open("aoc3input.txt", "r")
inputList = [x.rstrip("\n") for x in fileIn]
fileIn.close()

mostCommonBits = []

for column in range(len(inputList[0])):
    zeroCount = 0
    oneCount = 0
    for row in range(len(inputList)):
        if inputList[row][column] == "0":
            zeroCount += 1
        else:
            oneCount += 1
    if zeroCount > oneCount:
        mostCommonBits.append("0")
    else:
        mostCommonBits.append("1")
leastCommonBits = ["1" if x == "0" else "0" for x in mostCommonBits]

mostCommonBinary = "".join(mostCommonBits)
leastCommonBinary = "".join(leastCommonBits)
decimalMostCommon = int(mostCommonBinary,2)
decimalLeastCommon = int(leastCommonBinary,2)
print("rate:", decimalMostCommon*decimalLeastCommon)

# part 2

genRatingList = [x for x in inputList]
for column in range(len(inputList[0])):
    zeroCount = 0
    oneCount = 0
    for row in range(len(genRatingList)):
        if genRatingList[row][column] == "0":
            zeroCount += 1
        else:
            oneCount += 1
    if zeroCount > oneCount:
        for row in range(len(inputList)):
            if inputList[row][column] == "1":
                if inputList[row] in genRatingList:
                    genRatingList.remove(inputList[row])    
    else:
        for row in range(len(inputList)):
            if inputList[row][column] == "0":
                if inputList[row] in genRatingList:
                    genRatingList.remove(inputList[row])

coRatingList = [x for x in inputList]
for column in range(len(inputList[0])):
    zeroCount = 0
    oneCount = 0
    for row in range(len(coRatingList)):
        if coRatingList[row][column] == "0":
            zeroCount += 1
        else:
            oneCount += 1   
    if zeroCount <= oneCount:
        for row in range(len(inputList)):
            if inputList[row][column] == "1":
                if inputList[row] in coRatingList:
                    coRatingList.remove(inputList[row])    
    else:
        for row in range(len(inputList)):
            if inputList[row][column] == "0":
                if inputList[row] in coRatingList:
                    coRatingList.remove(inputList[row])
    if len(coRatingList) == 1:
        break

print(int(genRatingList[0],2)*int(coRatingList[0],2))

