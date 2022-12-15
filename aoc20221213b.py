from functools import cmp_to_key
from aoc20221213a import *


def parse(data):
    return [eval(l) for l in data.replace("\n\n", "\n").split("\n")]


def aoc(data):
    s = sorted(parse(data + "\n[[2]]\n[[6]]"), key=cmp_to_key(comp))
    return (s.index([[2]]) + 1) * (s.index([[6]]) + 1)
