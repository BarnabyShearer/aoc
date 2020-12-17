from aoc20201214a import parse


def bit_not(n, numbits=36):
    return (1 << numbits) - 1 - n


def stretch(n, mask, numbits=36):
    ni = 0
    result = 0
    for mask_i in range(numbits):
        if mask & 1 << mask_i:
            if n & 1 << ni:
                result |= 1 << mask_i
            ni += 1
    return result


def aoc(data):
    mem = {-1: 0, -2: 0}
    for add, val in parse(data):
        if add >= 0:
            add |= mem[-2]
            float = mem[-1] ^ mem[-2]
            add &= bit_not(float)
            for i in range(2 ** bin(float).count("1")):
                mem[add | stretch(i, float)] = val
        else:
            mem[add] = val
    del mem[-1]
    del mem[-2]
    return sum(mem.values())
