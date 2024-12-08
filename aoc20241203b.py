import re


def aoc(data):
    total = 0
    enabled = True
    for m in re.finditer(
        re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)"), data
    ):
        if m.group(0) == "do()":
            enabled = True
        elif m.group(0) == "don't()":
            enabled = False
        else:
            if enabled:
                total += int(m.group(1)) * int(m.group(2))
    return total
