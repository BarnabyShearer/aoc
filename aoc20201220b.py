import copy
from aoc20201220a import parse, borders

MAP = [(0, -1), (0, 1), (-1, 0), (1, 0)]
OP = [1, 0, 3, 2]


def rot(a):
    return a[2][::-1], a[3][::-1], a[1], a[0]


def flip(a):
    return a[0][::-1], a[1][::-1], a[3], a[2]


def options(b):
    return (
        b,
        rot(b),
        rot(rot(b)),
        rot(rot(rot(b))),
        flip(b),
        rot(flip(b)),
        rot(rot(flip(b))),
        rot(rot(rot(flip(b)))),
    )


def rotfull(tile):
    return tuple("".join(tuple(x)[::-1]) for x in zip(*tile))


def flipfull(tile):
    return (line[::-1] for line in tile)


def optionsfull(tile):
    return (
        tile,
        rotfull(tile),
        rotfull(rotfull(tile)),
        rotfull(rotfull(rotfull(tile))),
        flipfull(tile),
        rotfull(flipfull(tile)),
        rotfull(rotfull(flipfull(tile))),
        rotfull(rotfull(rotfull(flipfull(tile)))),
    )


def aoc(data):
    photo = {}
    tiles = {}
    for id, tile in parse(data):
        tiles[id] = options(borders(tile))

    used = set()
    photo[(0, 0)] = (id, tiles[id][0])
    used.add(id)

    while len(photo) < len(tiles):
        for (x, y), (id, tile) in copy.copy(photo).items():
            for d, border in enumerate(tile):
                dx, dy = MAP[d]
                if (x + dx, y + dy) in photo:
                    continue
                for nid, nborders in tiles.items():
                    if nid not in used and border in [k[OP[d]] for k in nborders]:
                        nnb = nborders[[k[OP[d]] for k in nborders].index(border)]
                        photo[(x + dx, y + dy)] = (nid, nnb)
                        used.add(nid)
                        break

    minx = min([x for x, y in photo.keys()])
    maxx = max([x for x, y in photo.keys()])
    miny = min([y for x, y in photo.keys()])
    maxy = max([y for x, y in photo.keys()])

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(f"{photo.get((x, y), (0,0))[0]:6}", end="")
        print()

    fulltiles = dict(parse(data))

    fullphoto = []
    for y in range(miny, maxy + 1):
        for i in range(1, 9):
            fullphoto.append("")
            for x in range(minx, maxx + 1):
                rot = tiles[photo[(x, y)][0]].index(photo[(x, y)][1])
                full = fulltiles[photo[(x, y)][0]]
                fullphoto[-1] += tuple(optionsfull(full)[rot])[i][1:9]

    fullphoto = rotfull(rotfull(rotfull(fullphoto)))

    ness = ("                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   ")

    total = 0
    for y in range(len(fullphoto) - 2):
        for x in range(len(fullphoto[0]) - 19):
            for yy, line in enumerate(ness):
                for xx, c in enumerate(line):
                    if c == "#" and fullphoto[y + yy][x + xx] != "#":
                        break
                else:
                    continue
                break
            else:
                total += 1
    return "".join(fullphoto).count("#") - "".join(ness).count("#") * total
