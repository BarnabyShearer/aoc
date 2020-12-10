import itertools
from cpu import cpu


def generator():
    while True:
        x = yield
        yield x


def aoc(data):
    max = 0
    for phase in itertools.permutations(range(5, 10)):
        amps = []
        for amp in range(5):
            c = cpu(data)
            next(c)
            c.send(phase[amp])
            amps.append(c)
        input = 0
        first = True
        try:
            while True:
                for amp in amps:
                    if not first:
                        next(amp)
                    input = amp.send(input)
                first = False
        except StopIteration:
            pass
        if input > max:
            max = input
    return max
