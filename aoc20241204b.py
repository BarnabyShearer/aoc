from aoc20241204a import g


def aoc(data):
    total = 0
    data = data.split("\n")
    for y, yy in enumerate(data):
        for x, xx in enumerate(yy):
            if xx == "A":
                if g(g(data, y - 1), x - 1) == "M" and g(g(data, y + 1), x + 1) == "S":
                    if (
                        g(g(data, y - 1), x + 1) == "M"
                        and g(g(data, y + 1), x - 1) == "S"
                    ):
                        total += 1
                    if (
                        g(g(data, y - 1), x + 1) == "S"
                        and g(g(data, y + 1), x - 1) == "M"
                    ):
                        total += 1
                if g(g(data, y - 1), x - 1) == "S" and g(g(data, y + 1), x + 1) == "M":
                    if (
                        g(g(data, y - 1), x + 1) == "M"
                        and g(g(data, y + 1), x - 1) == "S"
                    ):
                        total += 1
                    if (
                        g(g(data, y - 1), x + 1) == "S"
                        and g(g(data, y + 1), x - 1) == "M"
                    ):
                        total += 1
    return total
