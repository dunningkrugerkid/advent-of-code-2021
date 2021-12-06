fileIn = open("aoc6input.txt","r")
joined = fileIn.read()
listFish = joined.split(",")
listFish = [int(x) for x in listFish]

def reproduction(lst, numDays):
    if numDays < 0:
        return len(lst)
    lst2 = [x-1 for x in lst]
    for x in range(len(lst2)):
        if lst2[x] == -1:
            lst2[x] = 6
            lst2.append(8)
    return reproduction(lst2,numDays-1)

def main():
    keepGoing = True
    while keepGoing:
        try: 
            numDays = int(input("enter number of days: "))
            if numDays < 0:
                raise ValueError
            print(reproduction(listFish, numDays-1))
            keepGoing = False
        except ValueError:
            print("try again but better this time")


if __name__ == "__main__":
    main()


            