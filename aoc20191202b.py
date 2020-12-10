from cpu import cpu


def aoc(data):
    for noun in range(99):
        for verb in range(99):
            if next(cpu(data, [noun, verb])) == 19690720:
                return 100 * noun + verb
