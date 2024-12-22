from aoc20241217a import cpu, parse


def search(prog, out, A, B, C):
    if not out:
        return A
    for a in range(1024):
        if a >> 3 == A & 127 and next(cpu(prog, a, B, C)) == out[-1]:
            t = search(prog, out[:-1], (A << 3) | (a % 8), B, C)
            if t:
                return t


def aoc(data):
    prog, A, B, C = parse(data)
    return search(prog, prog, 0, B, C)
