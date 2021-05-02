#Opening and reading file
def readFile(fileName):
    inputFile = open(fileName, 'r')
    inputNumbers = inputFile.read().splitlines()
    inputFile.close()
    return inputNumbers

def findAns():
    numbersArray = readFile("inputDay3.txt")    #replace with your file with data
    result = 0
    position = 0
    for y in range(len(numbersArray)-1):
        mapLine = numbersArray[y]
        if position > 30:
            position = position - 31
        if mapLine[position] == "#":
            result = result + 1
        position = position + 3
    print(result)
findAns()