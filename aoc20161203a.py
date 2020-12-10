def parse(line):
    return [int(x) for x in line.split()]


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def aoc(data):
    return sum([is_triangle(*parse(line)) for line in data.split("\n")])
