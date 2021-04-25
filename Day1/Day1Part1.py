def readFile(fileName):
    inputFile = open(fileName, 'r')
    inputNumbers = inputFile.read().splitlines()
    inputFile.close()
    return inputNumbers

def findAns():
    numbersArray = readFile("input.txt")
    for y in range(len(numbersArray)):
        for x in range(len(numbersArray)):
            firstNum = numbersArray[x]
            secondNum =numbersArray[y]
            if int(firstNum) + int(secondNum) == 2020:
                result = int(firstNum) * int(secondNum)
                print(result)

findAns()