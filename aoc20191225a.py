from itertools import combinations

from cpu import cpu, read, write

PRE = """south
take fixed point
north
west
west
west
take hologram
east
east
east
north
take candy cane
west
take antenna
south
take whirled peas
north
west
take shell
east
east
north
north
take polygon
south
west
take fuel cell
west"""


def aoc(data):
    c = cpu(data)
    s, _ = read(c)
    inv = [
        line.split(maxsplit=1)[1] for line in PRE.split("\n") if line.startswith("take")
    ]
    print(inv)
    print(s)
    for line in PRE.split("\n"):
        s, _ = write(c, line + "\n")
        print(s)
    prev = inv
    for l in range(len(inv), 0, -1):
        for want in combinations(inv, l):
            for i in inv:
                if i in want and not i in prev:
                    write(c, f"take {i}\n")
                if i in prev and not i in want:
                    write(c, f"drop {i}\n")
            prev = want
            s, _ = write(c, "west\n")
            print(s)
            if "airlock" in s:
                return int(s.split()[-8])
