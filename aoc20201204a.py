def aoc(data):
    total = 0
    for passport in data.split("\n\n"):
        passport = " " + passport.replace("\n", " ")
        ok = True
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if f" {key}:" not in passport:
                ok = False
        if ok:
            total += 1
    return total
