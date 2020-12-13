from itertools import permutations
from cpu import cpu, read, write


def springbot(data, prog):
    c = cpu(data)
    read(c)
    _, last = write(c, prog)
    return last[0]


def ops(inputs):
    op = ["AND", "NOT", "OR"]
    outputs = "JT"
    for o in op:
        for a in inputs:
            for b in outputs:
                yield " ".join((o, a, b))


def randprog(data, inputs, start):
    for c in range(1, 12):
        for cmds in permutations(ops(inputs), c):
            # Never jump or walk into hole
            try:
                return springbot(
                    data,
                    "\n".join(cmds)
                    + f"""
AND D J
NOT A T
OR T J
{start}
""",
                )
            except IndexError:
                pass


def aoc(data):
    return randprog(data, "ABCD", "WALK")
