def parse(data):
    for line in data.split("\n"):
        add, val = line.split(" = ")
        if add == "mask":
            yield -1, int(val.replace("X", "1"), 2)
            yield -2, int(val.replace("X", "0"), 2)
        else:
            yield int(add.split("[")[-1][:-1]), int(val)


def aoc(data):
    mem = {-1: 0, -2: 0}
    for add, val in parse(data):
        mem[add] = val
        if add > 0:
            mem[add] &= mem[-1]
            mem[add] |= mem[-2]
    del mem[-1]
    del mem[-2]
    return sum(mem.values())
