def parse(data):
    for line in data.split("\n"):
        match line.split():
            case "up", amount:
                yield 0, -int(amount)
            case "down", amount:
                yield 0, int(amount)
            case "forward", amount:
                yield int(amount), 0


def aoc(data):
    x = y = 0
    for dx, dy in parse(data):
        x += dx
        y += dy
    return x * y
