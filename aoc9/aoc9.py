from math import prod
fileIn = open("aoc9input.txt","r")
matrix = [line.rstrip("\n") for line in fileIn] # formatting
fileIn.close()
for x in range(len(matrix)):
    matrix[x] = "9" + matrix[x] +"9" # adding nines to avoid the corner cases. all corners are now "9" which will never be local minimum
listMinimumHeights = []

def checkSides(line,index): # pass in a single line as string and the index of the value you want to check
    return True if line[index-1] > line[index] and line[index+1] > line[index] else False
            
def checkBelow(matrixSlice,index): # passing in two lines and index of value to check. line and line below it
    return True if matrixSlice[1][index] > matrixSlice[0][index] else False 
    
def checkAbove(matrixSlice,index): # similar to checkTop, but with line and line above it
    return True if matrixSlice[0][index] > matrixSlice[1][index] else False
# now comes the fun part
for row in range(len(matrix)):
    for digit in range(len(matrix[row])): # usual 2d list iteration shenanigans
        if row == 0: # don't care about looking up if you're already on top
            if checkSides(matrix[row],digit) and checkBelow(matrix[row:row+2],digit):
                listMinimumHeights.append(matrix[row][digit])          
        elif row == len(matrix)-1: # don't keep digging if you're at rock bottom
            if checkSides(matrix[row],digit) and checkAbove(matrix[row-1:row+1],digit):
                listMinimumHeights.append(matrix[row][digit])
        else: # these rows are in the middle of the pack
            if checkSides(matrix[row],digit) and checkAbove(matrix[row-1:row+1],digit) and checkBelow(matrix[row:row+2],digit):
                listMinimumHeights.append(matrix[row][digit])
print("risk level sum:", sum([int(x)+1 for x in listMinimumHeights])) # per puzzle instructions

def floodFill(i, j, lis): # courtesy to ripu for offering some insight here and on getBasin, this is a far more polished way to go about it
    if i < 0 or j < 0 or i >= len(lis) or j >= len(lis[0]):
        return 0
    try:
        if lis[i][j] == "9":
            return 0
        newStr = lis[i][:j] + "9" + lis[i][j+1:]
        lis[i] = newStr
        return 1 + floodFill(i+1, j, lis) + floodFill(i, j+1, lis) + floodFill(i-1, j, lis) + floodFill(i, j-1, lis)
    except IndexError:
        return 0
        
def getBasin():
    basins = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            basins.append(floodFill(i, j, matrix))
    basins = sorted(basins)
    return basins[-1] * basins[-2] * basins[-3]

print("product of basin sizes:",getBasin())



    

