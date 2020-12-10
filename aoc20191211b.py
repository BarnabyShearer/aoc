from aoc20191211a import robot


def aoc(data):
    prev = 0
    for (xx, yy), v in sorted(robot(data, {(0, 0): 1}).items()):
        if xx != prev:
            print()
            prev = xx
        print("█" if v else " ", end="")
    return input("Please enter what you see: ")
