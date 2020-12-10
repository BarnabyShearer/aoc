def check(line):
    return max(line) - min(line)


def aoc(data):
    return sum([check([int(x) for x in line.split()]) for line in data.split("\n")])
