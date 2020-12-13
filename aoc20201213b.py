from math import prod


def chinese_remainder(n, a):
    total = 0
    for ni, ai in zip(n, a):
        p = prod(n) // ni
        total += ai * pow(p, -1, ni) * p
    return total % prod(n)


def aoc(data):
    _, data = data.split()
    n = [int(b) for b in data.split(",") if b != "x"]
    a = [int(b) - i for i, b in enumerate(data.split(",")) if b != "x"]
    return chinese_remainder(n, a)
