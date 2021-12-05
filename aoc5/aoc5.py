from collections import defaultdict
fileIn = open("aoc5input.txt", "r")
D1 = defaultdict(int)
D2 = defaultdict(int)
for line in fileIn:
    initialPoint,endPoint = line.split("->")
    x1,y1 = initialPoint.split(",")
    x2,y2 = endPoint.split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    changeX = x2 - x1
    changeY = y2 - y1
    for i in range(max(abs(changeX), abs(changeY))+1):
        if (changeX>0):
            x = x1 + i
        else:
            if (changeX<0):
                x = x1 - i
            else:
                x = x1
        if changeY > 0:
            y = y1 + i
        else:
            if changeY<0:
                y = y1 - i
            else:
                y = y1
        if changeX == 0 or changeY == 0:
            D1[(x,y)] += 1
        D2[(x,y)] += 1
numNonDiag = 0
numDiagInc = 0
fileIn.close()
for val in D1:
    if D1[val]>1:
        numNonDiag += 1
for val in D2:
    if D2[val]>1:
        numDiagInc += 1
print("part 1 and part 2, respectively:", numNonDiag, numDiagInc)

