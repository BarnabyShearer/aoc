def check(line):
    for i, x in enumerate(line):
        for y in line[i + 1 :]:
            if x % y == 0:
                return x // y
            if y % x == 0:
                return y // x


def aoc(data):
    return sum([check([int(x) for x in line.split()]) for line in data.split("\n")])
