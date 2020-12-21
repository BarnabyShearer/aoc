import re


class N:
    def __init__(s, v):
        s.v = v

    def __mul__(s, o):
        return N(s.v * o.v)

    def __add__(s, o):
        return N(s.v + o.v)

    __truediv__ = __add__
    __sub__ = __mul__


def aoc(data, o={42: "*", 43: "/"}):
    return sum(
        eval(l).v for l in re.sub(r"(\d+)", r"N(\1)", data.translate(o)).split("\n")
    )
