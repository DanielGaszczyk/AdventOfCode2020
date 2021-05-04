import re


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
    p = "[\d]+"
    for y in range(len(numbers_array)):
        line = numbers_array[y]
        passport_data = passport_data + line
        if "\n" in line and not ":" in line:
            fields_number = sum(
                passport_data.count(x) for x in ("byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"))
            if fields_number >= 7:

                # preparing string to spliting
                passport_data = passport_data.replace(":", " ")
                passport_data = passport_data.replace("\n", " ")
                passport_data = passport_data.split(" ")

                # Finding data and key after splitting
                byr_valid = 1920 <= int(passport_data[passport_data.index("byr") + 1]) <= 2002
                iyr_valid = 2010 <= int(passport_data[passport_data.index("iyr") + 1]) <= 2020
                eyr_valid = 2020 <= int(passport_data[passport_data.index("eyr") + 1]) <= 2030
                pid_valid = (9 == len(passport_data[passport_data.index("pid") + 1])) and (
                    passport_data[passport_data.index("pid") + 1]).isnumeric()

                # Eyes color check
                ecl_valid = (sum(passport_data[passport_data.index("ecl") + 1].count(x) for x in
                                 ("amb", "blu", "brn", "gry", "hzl", "grn", "oth"))) == 1

                # Height check
                if re.search(p, passport_data[passport_data.index("hgt") + 1]) is not None:
                    for catch in re.finditer(p, passport_data[passport_data.index("hgt") + 1]):
                        if passport_data[passport_data.index("hgt") + 1].count("cm") == 1:
                            hgt_valid = 150 <= int(catch[0]) <= 193
                        elif passport_data[passport_data.index("hgt") + 1].count("in") == 1:
                            hgt_valid = 59 <= int(catch[0]) <= 76
                        else:
                            hgt_valid = 0
                else:
                    hgt_valid = 0

                # hcl_valid check
                try:
                    hcl_valid = int(passport_data[passport_data.index("hcl") + 1][1:], 16) != 0 and (
                            passport_data[passport_data.index("hcl") + 1][0] == "#") and (
                                    len(passport_data[passport_data.index("hcl") + 1])) == 7
                except ValueError:
                    hcl_valid = False

                # Result checking
                data_check = byr_valid + iyr_valid + hcl_valid + hgt_valid + ecl_valid + pid_valid + eyr_valid
                if data_check == 7:
                    result = result + 1
            passport_data = ""
    print(result)


find_ans()
