from aoc20201201a import two_sum


def aoc(input):
    data = [int(n) for n in input.split("\n")]
    for i, a in enumerate(data):
        try:
            b, c = two_sum(data[i + 1 :], 2020 - a)
            return a * b * c
        except TypeError:
            pass
