fileIn = open("aoc1input.txt","r")
listOfDepths = [eval(x) for x in fileIn]
fileIn.close()
numIncreases = 0

slide1 = listOfDepths[0] + listOfDepths[1] + listOfDepths[2]
for i in range(1, len(listOfDepths)-2):
    slide2 = listOfDepths[i] + listOfDepths [i+1] + listOfDepths[i+2]
    if slide2 > slide1:
        numIncreases += 1
    slide1 = slide2

print("number of increases:", numIncreases)

