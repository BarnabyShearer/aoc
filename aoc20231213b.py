from aoc20231213a import *


def aoc(data):
    total = 0
    for i, p in enumerate(parse(data)):
        aa = next(reflect(p), 0)
        bb = next(reflect(tuple("".join(c) for c in zip(*p))), 0)
        for y in range(len(p)):
            for x in range(len(p[0])):
                pp = p.copy()
                pp[y] = pp[y][:x] + ("." if pp[y][x] == "#" else "#") + pp[y][x + 1 :]
                for a in reflect(pp):
                    if a > 0 and a != aa:
                        total += 100 * a
                        break
                else:
                    for b in reflect(tuple("".join(c) for c in zip(*pp))):
                        if b > 0 and b != bb:
                            total += b
                            break
                    else:
                        continue
                    break
                break
            else:
                continue
            break
    return total
