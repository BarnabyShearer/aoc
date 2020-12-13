from aoc20191223a import init, step


def aoc(data):
    prev = None
    nat = (0, 0)
    buf, cpus = init(data)
    while True:
        ret = step(buf, cpus)
        if ret:
            nat = ret
        else:
            if nat[1] == prev:
                return prev
            prev = nat[1]
            buf[0].append(nat)
