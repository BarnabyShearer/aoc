def do_line(p, line, match):
    while True:
        for m, i in match.items():
            if line.startswith(m) or line.startswith(m[::-1]):
                return i * 10**p
        line = line[1:]


def do(data, match):
    total = 0
    for l in data.split("\n"):
        for p, ll in enumerate((l[::-1], l)):
            total += do_line(p, ll, match)
    return total


def aoc(data):
    return do(data, {str(x): x for x in range(10)})
