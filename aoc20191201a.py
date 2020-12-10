def aoc(data):
    return sum([int(x) // 3 - 2 for x in data.split("\n")])
