from operator import gt, lt, eq
from math import prod
from aoc20211216a import *

OPS = {
    0: lambda *a: sum(a),
    1: lambda *a: prod(a),
    2: lambda *a: min(a),
    3: lambda *a: max(a),
    5: gt,
    6: lt,
    7: eq,
}


def compute(ver, op, sub, length):
    return (
        ver,
        op,
        OPS[op](*(val for _, __, val, ___ in sub)),
        length,
    )


def aoc(data):
    return next(packets(parse(data), compute))[2]
