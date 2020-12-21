import re

rules = {}


class Add:
    def __init__(self, a, b=""):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"{rules.get(self.a, self.a)}{rules.get(self.b, self.b)}"


class Or(Add):
    def __repr__(self):
        return f"(({self.a})|({self.b}))"


def rule(line):
    if '"' in line:
        return line[1]
    elif "|" in line:
        return Or(
            *(Add(*(int(x) for x in subrule.split())) for subrule in line.split(" | "))
        )
    else:
        return Add(*(int(x) for x in line.split()))


def parse(data):
    global rules
    rules, msgs = data.split("\n\n")
    rules = {
        int(line.split(":")[0]): rule(line.split(": ")[1]) for line in rules.split("\n")
    }
    msgs = msgs.split()
    return rules, msgs


def aoc(data):
    rules, msgs = parse(data)
    rule = re.compile(str(rules[0]))
    return sum(True for msg in msgs if rule.fullmatch(msg))
