from aoc20191217a import camera

from cpu import cpu


def find_path(screen):
    w = screen.index("\n") + 1
    map = [-w, 1, w, -1]
    dir = 0
    pos = screen.index("^")
    moves = []

    def look(dir):
        at = pos + map[dir % 4]
        return 0 <= at < len(screen) and screen[at] == "#"

    # Assume we always turn once and then move as far as we can
    while True:
        if look(dir):
            pos += map[dir % 4]
            moves[-1] += 1
        elif look(dir + 1):
            dir += 1
            moves.append("R")
            moves.append(0)
        elif look(dir - 1):
            dir -= 1
            moves.append("L")
            moves.append(0)
        else:
            break
    return moves


def find_short(moves):
    for i in range(1, 10):
        a = moves[:i]
        for ii in range(i + 1, i + 10):
            b = moves[i:ii]
            m = []
            c = []
            iii = 0
            cdone = False
            while True:
                if len(m) > 10:
                    break
                if iii == len(moves):
                    return [m, a, b, c, ["n"]]
                if moves[iii : iii + len(a)] == a:
                    cdone = "C" in m
                    m.append("A")
                    iii += len(a)
                elif moves[iii : iii + len(b)] == b:
                    cdone = "C" in m
                    m.append("B")
                    iii += len(b)
                elif cdone and moves[iii : iii + len(c)] == c:
                    m.append("C")
                    iii += len(c)
                elif cdone:
                    break
                else:
                    if "C" not in m:
                        m.append("C")
                    c.append(moves[iii])
                    iii += 1


def aoc(data):
    progs = [
        ",".join([str(op) for op in prog]) + "\n"
        for prog in find_short(find_path(camera(data)))
    ]
    c = cpu("2" + data[1:])
    for prog in progs:
        while next(c):
            pass
        [c.send(ord(s)) for s in prog]
    try:
        while True:
            last = next(c)
    except:
        pass
    return last
