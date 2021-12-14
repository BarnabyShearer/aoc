from collections import Counter
from aoc20211201a import window
from copy import copy


def parse(data):
    code, pairs = data.split("\n\n")
    code = Counter(tuple("".join(c) for c in window(" " + code + " ")))
    pairs = {
        k: (k[0] + v, v + k[1]) for k, v in (p.split(" -> ") for p in pairs.split("\n"))
    }
    return code, pairs


def polymerize(code, pairs):
    for k, v in copy(code).items():
        if k in pairs:
            for kk in pairs[k]:
                code[kk] += v
            code[k] -= v
    return code


def score(code):
    freq = Counter()
    for k, v in code.items():
        freq[k[0]] += v
        freq[k[1]] += v
    for f in freq:
        freq[f] //= 2
    del freq[" "]
    return max(freq.values()) - min(freq.values())


def aoc(data):
    code, pairs = parse(data)
    for _ in range(10):
        code = polymerize(code, pairs)
    return score(code)
