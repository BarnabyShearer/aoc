def parse(data):
    order, data = data.split("\n\n")
    order = [l.split("|") for l in order.split("\n")]
    data = [l.split(",") for l in data.split("\n")]
    return order, data


def aoc(data):
    order, data = parse(data)
    total = 0
    for l in data:
        for a, b in order:
            if a in l and b in l:
                if l.index(a) > l.index(b):
                    break
        else:
            total += int(l[(len(l) - 1) // 2])
    return total
