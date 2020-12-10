from aoc20201208a import parse, run

MAP = {"jmp": "nop", "nop": "jmp", "acc": "acc"}


def aoc(data):
    prog = parse(data)
    for i, (opp, par) in enumerate(prog):
        fix = prog.copy()
        fix[i] = (MAP[opp], par)
        success, acc = run(fix)
        if success:
            return acc
