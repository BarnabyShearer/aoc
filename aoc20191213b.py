from cpu import cpu
from aoc20191213a import draw


def aoc(data):
    c = cpu("2" + data[1:])
    screen = {}
    try:
        while True:
            x = next(c)
            if x is None:
                draw(screen)
                move = 0
                objs = dict(map(reversed, screen.items()))
                if objs[4][0] < objs[3][0]:
                    move = -1
                if objs[4][0] > objs[3][0]:
                    move = 1
                x = c.send(move)
            y = next(c)
            v = next(c)
            screen[(x, y)] = v
    except StopIteration:
        pass
    return screen[(-1, 0)]
