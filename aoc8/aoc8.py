from itertools import permutations
fileIn = open("aoc8input.txt","r")

uniqueCount = 0
totalCount = 0

for x in fileIn:
    left,right = x.split(" | ")
    listLeft = left.split()
    listRight = right.split()
    zero = ""
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    eight = ""
    nine = ""

    for x in listRight:
        if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
            uniqueCount += 1
    for x in listLeft: # cover the unique ones first
        if len(x) == 2:
            one = x
        elif len(x) == 3:
            seven = x
        elif len(x) == 4:
            four = x
        elif len(x) == 7:
            eight = x

    for x in listLeft:
        if len(x) == 6: # possibilties are zero, nine, six
            total = 0 # count unique segment overlaps with seven and four in an imaginary display
            for digit in x:
                if digit in seven or digit in four:
                    total += 1
            if total == 4 and one[0] in x and one[1] in x:
                zero = x
            elif total == 5:
                nine = x
            else:
                six = x
        elif len(x) == 5: # possibilities are two, three, five
            total = 0 # count overlaps with four. 
            if one[0] in x and one[1] in x:
                three = x # three is the only possibility that encompasses both of one's segments
            else:
                for digit in x: # 5 will contain 3 elements of 4, 2 will contain 2
                    if digit in four:
                        total +=1
                if total == 3:
                    five = x
                else:
                    two = x      
    returnValList = []
    for key in listRight:
        for possibility in listLeft:
            permutationList = [''.join(x) for x in permutations(key)]
            for permutation in permutationList:
                if permutation == possibility:
                    returnValList.append(possibility)
    for x in range(len(returnValList)):
        if returnValList[x] == zero:
            returnValList[x] = "0"
        elif returnValList[x] == one:
            returnValList[x] = "1"
        elif returnValList[x] == two:
            returnValList[x] = "2"
        elif returnValList[x] == three:
            returnValList[x] = "3"
        elif returnValList[x] == four:
            returnValList[x] = "4"
        elif returnValList[x] == five:
            returnValList[x] = "5"
        elif returnValList[x] == six:
            returnValList[x] = "6"
        elif returnValList[x] == seven:
            returnValList[x] = "7"
        elif returnValList[x] == eight:
            returnValList[x] = "8"
        elif returnValList[x] == nine:
            returnValList[x] = "9"
    presentCount = int("".join(returnValList))
    totalCount += presentCount

print("digit instances with unique segment counts:", uniqueCount)
print("sum of all output:", totalCount)