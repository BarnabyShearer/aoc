def aoc(data):
    floor = 0
    for i, c in enumerate(data):
        floor += -1 if c == ")" else 1
        if floor == -1:
            return i + 1
