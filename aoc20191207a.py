import itertools
from cpu import cpu


def aoc(data):
    max = 0
    for phase in itertools.permutations(range(5)):
        output = 0
        for amp in range(5):
            c = cpu(data)
            next(c)
            c.send(phase[amp])
            output = c.send(output)
        if output > max:
            max = output
    return max
