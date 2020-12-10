from aoc20201205a import seats


def aoc(data):
    next = 0
    for seat in sorted(seats(data)):
        if seat == next:
            return seat - 1
        next = seat + 2
