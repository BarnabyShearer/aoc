from aoc20211208a import *

KOWN = {2: 1, 3: 7, 4: 4, 7: 8}


def key(a):
    l = {KOWN[len(c)]: c for c in a if len(c) in KOWN}
    for c in a:
        if len(c) == 5:
            l[3 if len(c - l[1]) == 3 else 5 if len(c - l[4]) == 2 else 2] = c
        elif len(c) == 6:
            l[9 if len(c - l[4]) == 2 else 0 if len(c - l[7]) == 3 else 6] = c
    return {v: k for k, v in l.items()}


def convert(key, b):
    total = 0
    for d in b:
        total = total * 10 + key[d]
    return total


def aoc(data):
    total = 0
    for a, b in parse(data):
        total += convert(key(a), b)
    return total
