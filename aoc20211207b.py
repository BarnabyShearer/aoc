from aoc20211207a import *


def triangular_number(n):
    return (n * (n + 1)) // 2


def aoc(data):
    return min(moves(parse(data), triangular_number))
