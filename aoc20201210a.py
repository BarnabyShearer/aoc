def aoc(data):
    jolts = 0
    ones = 0
    threes = 1
    for psu in sorted([int(i) for i in data.split()]):
        if psu == jolts + 1:
            ones += 1
        if psu == jolts + 3:
            threes += 1
        jolts = psu
    return ones * threes
