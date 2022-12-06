from aoc20211201a import window


def aoc(data, n=4):
    for i, a in enumerate(window(data, n)):
        if len(set(a)) == n:
            return i + n
