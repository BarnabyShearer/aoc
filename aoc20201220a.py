from math import prod


def parse(data):
    for tile in data.split("\n\n"):
        _, id, *lines = tile.split()
        yield int(id[:-1]), lines


def borders(tile):
    return (
        tile[0],
        tile[-1],
        "".join([line[0] for line in tile]),
        "".join([line[-1] for line in tile]),
    )


def corners(data):
    tiles = {}
    for id, tile in parse(data):
        for border in borders(tile):
            for b in (border, border[::-1]):
                if b in tiles:
                    del tiles[b]
                    break
            else:
                tiles[border] = id
    result = set()
    for id in tiles.values():
        if list(tiles.values()).count(id) > 1:
            result.add(id)
    return result, tiles


def aoc(data):
    return prod(corners(data)[0])
