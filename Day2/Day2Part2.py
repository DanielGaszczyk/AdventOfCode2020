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
        firstNumber = dividedString[0]
        secondNumber = dividedString[1]
        neededChar = dividedString[2]
        password = dividedString[3]

        #Our neededChar is on firstNumber or secondNumber position in password (not both!)
        if (password[int(firstNumber)-1] == neededChar) is not (password[int(secondNumber)-1] == neededChar):
            result = result+1
    print(result)
findAns()