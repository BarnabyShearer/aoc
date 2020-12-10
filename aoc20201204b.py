def aoc(data):
    total = 0
    for passport in data.split("\n\n"):
        valid = 0
        for key, value in [item.split(":") for item in passport.split()]:
            if key == "byr" and 1920 <= int(value) <= 2002:
                valid += 1
            if key == "iyr" and 2010 <= int(value) <= 2020:
                valid += 1
            if key == "eyr" and 2020 <= int(value) <= 2030:
                valid += 1
            if key == "hgt":
                if value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193:
                    valid += 1
                if value[-2:] == "in" and 59 <= int(value[:-2]) <= 76:
                    valid += 1
            if (
                key == "hcl"
                and len(value) == 7
                and value[0] == "#"
                and set(value[1:]) - set("01234567891920abcdef") == set()
            ):
                valid += 1
            if key == "ecl" and value in (
                "amb",
                "blu",
                "brn",
                "gry",
                "grn",
                "hzl",
                "oth",
            ):
                valid += 1
            if (
                key == "pid"
                and len(value) == 9
                and set(value) - set("0123456789") == set()
            ):
                valid += 1
        if valid == 7:
            total += 1
    return total
