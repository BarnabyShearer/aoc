import operator


def parse(data):
    return [
        tuple(tuple(int(c) for c in l.split(",")) for l in s.split("\n")[1:])
        for s in data.split("\n\n")
    ]


def rot_x(cords):
    return tuple((x, z, -y) for x, y, z in cords)


def rot_y(cords):
    return tuple((z, y, -x) for x, y, z in cords)


def rot_z(cords):
    return tuple((y, -x, z) for x, y, z in cords)


def rep(f, n, arg):
    for _ in range(n):
        arg = f(arg)
    return arg


def rots(cords):
    for rx in range(2):
        for ry in range(4) if not rx else (0, 2):
            for rz in range(4):
                yield rep(rot_x, rx, rep(rot_y, ry, rep(rot_z, rz, cords)))


def sub(a, b):
    return tuple(map(operator.sub, a, b))


def add(a, b):
    return tuple(map(operator.add, a, b))


def find(beacons, s):
    for r in rots(s):
        for b in beacons:
            for bb in r[:-12]:
                off = sub(b, bb)
                match = 0
                for bbb in r:
                    if add(bbb, off) in beacons:
                        match += 1
                        if match == 12:
                            break
                else:
                    continue
                return off, tuple(add(bbb, off) for bbb in r)
    return None, None


def slam(data):
    beacons = set(data.pop(0))
    sensors = set()
    while data:
        for i, s in enumerate(data):
            sensor, found = find(beacons, s)
            if sensor:
                sensors.add(sensor)
                beacons.update(found)
                del data[i]
                print(f"Found {len(beacons)} with {len(sensors)}")
    return sensors, beacons


def aoc(data):
    return len(slam(parse(data))[1])
