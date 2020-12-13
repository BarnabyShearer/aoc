from cpu import cpu


def init(data):
    buf = []
    for _ in range(50):
        buf.append([])
    cpus = [cpu(data) for _ in range(50)]
    [next(c) for c in cpus]
    [c.send(i) for i, c in enumerate(cpus)]
    return buf, cpus


def step(buf, cpus):
    while True:
        for i, c in enumerate(cpus):
            t = c.send(-1)
            if not t and len(buf[i]) > 0:
                x, y = buf[i].pop(0)
                c.send(x)
                t = c.send(y)
            if t == 255:
                return next(c), next(c)
            if t:
                buf[t].append((next(c), next(c)))
        if not any(buf):
            return


def aoc(data):
    return step(*init(data))[1]
