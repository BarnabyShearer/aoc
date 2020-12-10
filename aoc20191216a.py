from itertools import repeat, cycle, chain


def fft(input):
    for i in range(1, len(input) + 1):
        x = cycle(chain(repeat(0, i), repeat(1, i), repeat(0, i), repeat(-1, i)))
        next(x)
        yield abs(sum([a * b for a, b in zip(x, input)])) % 10


def aoc(data):
    x = [int(x) for x in data]
    for phase in range(100):
        x = list(fft(x))
    return int("".join([str(a) for a in x[:8]]))
