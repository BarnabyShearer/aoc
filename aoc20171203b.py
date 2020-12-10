from aoc20171203a import spiral


def aoc(data):
    mem = {(0, 0): 1}
    for x, y in spiral(int(data)):
        sum = 0
        for xx in range(-1, 2):
            for yy in range(-1, 2):
                sum += mem.get(((x + xx), (y + yy)), 0)
        if sum > int(data):
            return sum
        mem[(x, y)] = sum
