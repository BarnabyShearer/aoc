from aoc20231208a import *
from math import lcm


def aoc(data):

    len_d, dir, nodes = parse(data)
    ghosts = [[(node, 0)] for node in nodes.keys() if node[-1] == "A"]
    loops = set()
    for s, d in enumerate(dir, 1):
        if not ghosts:
            break
        for g in ghosts.copy():
            next_step = (nodes[g[-1][0]][d], s % len_d)
            if next_step in g:
                ghosts.remove(g)
                # HACK: Took pity on us?
                assert [i for i, s in enumerate(g) if s[0][-1] == "Z"][0] == len(
                    g
                ) - g.index(next_step)
                loops.add(len(g) - g.index(next_step))
            g.append(next_step)
    total = 1
    for g in loops:
        total = lcm(total, g)
    return total
