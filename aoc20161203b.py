from aoc20161203a import parse, is_triangle


def aoc(data):
    total = 0
    for group in list(zip(*[iter(data.split("\n"))] * 3)):
        a, b, c = [parse(line) for line in group]
        for i in range(len(a)):
            if is_triangle(a[i], b[i], c[i]):
                total += 1
    return total
