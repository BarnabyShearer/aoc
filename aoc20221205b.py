from aoc20221205a import *


def aoc(data):
    creates, ins = parse(data)
    for c, a, b in ins:
        creates[b].extend(creates[a][-c:])
        del creates[a][-c:]
    return output(creates)
