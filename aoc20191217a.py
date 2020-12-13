from cpu import cpu, read


def camera(data):
    output, _ = read(cpu(data))
    return output


def aoc(data):
    screen = camera(data)
    print(screen)
    total = 0
    for y, line in enumerate(screen.split("\n")):
        w = len(line) + 1
        for x, char in enumerate(line):
            if all(
                [
                    y * w + x + t < len(screen) and screen[y * w + x + t] == "#"
                    for t in [-w, 1, 0, 1, w]
                ]
            ):
                total += x * y
    return total
