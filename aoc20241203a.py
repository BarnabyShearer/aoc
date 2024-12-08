import re


def aoc(data):
    total = 0
    for m in re.finditer(re.compile(r"mul\((\d{1,3}),(\d{1,3})\)"), data):
        total += int(m.group(1)) * int(m.group(2))
    return total
