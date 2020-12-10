def parse(line):
    range, let, passwd = line.split()
    return [int(x) for x in range.split("-")], let[0], passwd


def aoc(input):
    good = 0
    for [a, b], let, passwd in [parse(n) for n in input.split("\n")]:
        if a <= passwd.count(let) <= b:
            good += 1
    return good
