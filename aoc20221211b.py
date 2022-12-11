from aoc20221211a import *


def aoc(data):
    monkeys = parse(data)
    calm = 1
    for m in monkeys:
        calm *= m[2]
    return game(monkeys, 10000, lambda x: x % calm)
