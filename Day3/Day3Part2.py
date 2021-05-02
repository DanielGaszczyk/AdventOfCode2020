# Opening and reading file
def read_file(file_name):
    input_file = open(file_name, 'r')
    input_numbers = input_file.read().splitlines()
    input_file.close()
    return input_numbers


# Calculating full answer
def find_ans():
    first_val = travel7right1down()
    second_val = travel1right2down()
    third_val = travel1right1down()
    fourth_val = travel5right1down()
    fifth_val = travel3right1down()
    print(first_val * second_val * third_val * fourth_val * fifth_val)


def travel1right1down():
    numbers_array = read_file("inputDay3.txt")  # replace with your file with data
    result = 0
    position = 0
    for y in range(len(numbers_array) - 1):
        map_line = numbers_array[y]
        if position > 30:
            position = position - 31
        if map_line[position] == "#":
            result = result + 1
        position = position + 1
    return result


def travel5right1down():
    numbers_array = read_file("inputDay3.txt")  # replace with your file with data
    result = 0
    position = 0
    for y in range(len(numbers_array) - 1):
        map_line = numbers_array[y]
        if position > 30:
            position = position - 31
        if map_line[position] == "#":
            result = result + 1
        position = position + 5
    return result


def travel7right1down():
    numbers_array = read_file("inputDay3.txt")  # replace with your file with data
    result = 0
    position = 0
    for y in range(len(numbers_array) - 1):
        map_line = numbers_array[y]
        if position > 30:
            position = position - 31
        if map_line[position] == "#":
            result = result + 1
        position = position + 7
    return result


def travel1right2down():
    numbers_array = read_file("inputDay3.txt")  # replace with your file with data
    result = 0
    position = 0
    for y in range(len(numbers_array) - 1):
        if y % 2 == 1:
            continue
        map_line = numbers_array[y]
        if position > 30:
            position = position - 31
        if map_line[position] == "#":
            result = result + 1
        position = position + 1
    return result


def travel3right1down():
    numbers_array = read_file("inputDay3.txt")  # replace with your file with data
    result = 0
    position = 0
    for y in range(len(numbers_array) - 1):
        map_line = numbers_array[y]
        if position > 30:
            position = position - 31
        if map_line[position] == "#":
            result = result + 1
        position = position + 3
    return result


find_ans()
