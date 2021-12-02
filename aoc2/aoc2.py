# part 1
fileIn = open("aoc2input.txt","r")
listDirections = [x.rstrip("\n") for x in fileIn]
fileIn.close()
horizontalSum = 0
verticalSum = 0
for direction in range(len(listDirections)):
    depth = listDirections[direction][-1]
    if listDirections[direction][0] == "f":
        horizontalSum += int(depth)
    elif listDirections[direction][0] == "d":
        verticalSum += int(depth)
    elif listDirections[direction][0] == "u":
        verticalSum -= int(depth)
print("product:", horizontalSum*verticalSum)

# part 2
fileIn = open("aoc2input.txt","r")
listDirections = [x.rstrip("\n") for x in fileIn]
fileIn.close()
horizontalSum = 0
aim = 0
depth = 0
for direction in range(len(listDirections)):
    val = listDirections[direction][-1]
    if listDirections[direction][0] == "f":
        horizontalSum += int(val)
        depth += int(val)*aim
    elif listDirections[direction][0] == "d":
        aim += int(val)
    elif listDirections[direction][0] == "u":
        aim -= int(val)
print("product:", horizontalSum*depth)