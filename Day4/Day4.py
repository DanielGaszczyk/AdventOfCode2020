# Opening and reading file
def read_file(file_name):
    input_file = open(file_name, 'r')
    input_numbers = input_file.read().splitlines(True)
    input_file.close()
    return input_numbers


def find_ans():
    numbers_array = read_file("dataDay4.txt")  # Replace with your file with data
    result = 0  # Number of valid passports
    passport_data = ""
    for y in range(len(numbers_array)):
        line = numbers_array[y]
        passport_data = passport_data + line
        if "\n" in line and not ":" in line:
            fields_number = sum(
                passport_data.count(x) for x in ("byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"))
            if fields_number >= 7:
                result = result + 1
            passport_data = ""
    print(result)


find_ans()
