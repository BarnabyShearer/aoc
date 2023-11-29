from aoc20221221a import *


def aoc(data):
    lookup = parse(data)
    lookup["humn"] = "1j"
    lhs, _, rhs = lookup["root"].split()
    exec(order(lookup), globals())
    lhs, rhs = eval(lhs), eval(rhs)
    return int((rhs - lhs.real) / lhs.imag)
