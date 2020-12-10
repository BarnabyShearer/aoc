import math

from aoc20191212a import parse, step


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def aoc(data):
    moon = [m + [0, 0, 0] for m in parse(data)]
    phase = [set(), set(), set()]
    for d in range(3):
        while True:
            state = tuple((m[d], m[d + 3]) for m in moon)
            if state in phase[d]:
                break
            phase[d].add(state)
            step(moon, d)
    # Assume first repeat is initial state
    return lcm(lcm(len(phase[0]), len(phase[1])), len(phase[2]))
