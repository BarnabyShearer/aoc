def aoc(data):
    jolts = 0
    ones = 0
    total = 1
    for psu in sorted([int(i) for i in data.split()]) + [999999]:
        if psu == jolts + 1:
            ones += 1
        elif ones > 0:
            total *= 2 ** (ones - 1) - (2 ** (ones - 4) if ones > 3 else 0)
            ones = 0
        jolts = psu
    return total
