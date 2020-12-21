import re
from aoc20201219a import Add, Or, parse


class Repeat(Add):
    def __repr__(self):
        return f"({self.a})+"


def aoc(data):
    rules, msgs = parse(data)

    rules[8] = Repeat(rules[42])

    a = rules[42]
    b = rules[31]
    for _ in range(10):
        a = Add(a, rules[42])
        b = Add(b, rules[31])
        rules[11] = Or(rules[11], Add(a, b))

    rule = re.compile(str(rules[0]))
    return sum(True for msg in msgs if rule.fullmatch(msg))
