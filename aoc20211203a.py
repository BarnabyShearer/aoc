from statistics import multimode


def parse(data):
    return [int(l, base=2) for l in data.split()]


def most_common_bit(data, bit):
    return max(multimode(v & 1 << bit for v in data))


def most_common(data):
    return sum(most_common_bit(data, bit) for bit in range(12))


def aoc(data):
    gamma = most_common(parse(data))
    return gamma * (gamma ^ (2**12 - 1))
