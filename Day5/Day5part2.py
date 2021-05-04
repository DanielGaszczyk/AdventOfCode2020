import math


# Opening and reading file
def read_file(file_name):
    input_file = open(file_name, 'r')
    input_numbers = input_file.read().splitlines(True)
    input_file.close()
    return input_numbers


# F means "front", B means "back", L means "left", and R means "right".
def find_ans():
    numbers_array = read_file("dataDay5.txt")  # Replace with your file with data
    result = 0  # Number of highest ID
    boardlist = [1000]
    for x in range(len(numbers_array) - 1):
        line = numbers_array[x]
        row = [0, 127]
        column = [0, 7]

        for y in range(len(line)):
            space_char = line[y]
            if space_char == "F":
                row[1] = math.floor((row[1] + row[0]) / 2)
            elif space_char == "B":
                row[0] = math.ceil((row[1] + row[0]) / 2)
            elif space_char == "R":
                column[0] = math.ceil((column[1] + column[0]) / 2)
            elif space_char == "L":
                column[1] = math.floor((column[1] + column[0]) / 2)

        boardlist.append(row[1] * 8 + column[1])

    boardlist.sort()
    for z in range(1, len(boardlist)-2):
        if boardlist[z] != (boardlist[z + 1] - 1):
            result = boardlist[z]
            # print(boardlist[z])
        if boardlist[z] != (boardlist[z-1]+1):
            result = boardlist[z] + result
            # print(boardlist[z])
    print(math.ceil(result/2))  # End result of exercise


find_ans()
