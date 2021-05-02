# Opening, reading file and closing file
def readFile(fileName):
    inputFile = open(fileName, 'r')
    inputNumbers = inputFile.read().splitlines()
    inputFile.close()
    return inputNumbers


numbersArray = readFile("input.txt")  # insert your input data file
for x in range(len(numbersArray)):
    for y in range(len(numbersArray)):
        for z in range(len(numbersArray)):
            firstNum = numbersArray[x]
            secondNum = numbersArray[y]
            thirdNum = numbersArray[z]
            if int(firstNum) + int(secondNum) + int(thirdNum) == 2020:
                result = int(firstNum) * int(secondNum) * int(thirdNum)
                print(result)
