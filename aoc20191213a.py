import sys

from cpu import cpu

PALLET = " █▀▔@?????"
CLEAR = False


def draw(screen):
    global CLEAR
    if CLEAR:
        for _ in range(max(screen.keys())[1] + 2):
            sys.stdout.write("\033[F")
    for y in range(max(screen.keys())[1] + 1):
        for x in range(max(screen.keys())[0] + 1):
            print(PALLET[screen.get((x, y), 0)], end="")
        print()
    print(screen.get((-1, 0), 0))
    CLEAR = True


def aoc(data):
    c = cpu(data)
    screen = {}
    try:
        while True:
            x = next(c)
            y = next(c)
            v = next(c)
            screen[(x, y)] = v
    except StopIteration:
        pass
    draw(screen)
    return list(screen.values()).count(2)
