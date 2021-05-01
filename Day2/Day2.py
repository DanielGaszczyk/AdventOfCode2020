#Opening and reading file
def readFile(fileName):
    inputFile = open(fileName, 'r')
    inputNumbers = inputFile.read().splitlines()
    inputFile.close()
    return inputNumbers

def findAns():
    numbersArray = readFile("inputDay2.txt")    #replace with your file with data
    result = 0
    for y in range(len(numbersArray)-1):
        stringToDivide = numbersArray[y]
        #preparing string to spliting
        stringToDivide = stringToDivide.replace(':','')
        stringToDivide = stringToDivide.replace('-',' ')
        dividedString = stringToDivide.split(" ")
        #Placing divided strings and chars into variables
        atLeastNumber = dividedString[0]
        mostNumber = dividedString[1]
        neededChar = dividedString[2]

        # the frequency of occurrence of the sign in between atLeastNumber and mostNumber
        if int(atLeastNumber) <= (stringToDivide.count(neededChar)-1) <= int(mostNumber):
            result = result+1
    print(result)
findAns()