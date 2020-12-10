def parse(data):
    return [(line.split()[0], int(line.split()[1])) for line in data.split("\n")]


def run(prog):
    seen = set()
    pc = 0
    acc = 0
    while pc < len(prog):
        if pc in seen:
            return False, acc
        seen.add(pc)
        if prog[pc][0] == "acc":
            acc += prog[pc][1]
        elif prog[pc][0] == "jmp":
            pc += prog[pc][1] - 1
        pc += 1
    return True, acc


def aoc(data):
    _, acc = run(parse(data))
    return acc
