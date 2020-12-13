from aoc20191219a import tractor


def aoc(data):
    beam = [(0, 0), (0, 0), (0, 0), (0, 0), (4, 4)]
    while True:
        left, right = beam[-1]
        while not tractor(data, left, len(beam)):
            left += 1
        right += 1
        while tractor(data, right, len(beam)):
            right += 1
        beam.append((left, right - 1))
        if len(beam) >= 100 and left + 99 <= beam[-100][1]:
            return left * 10000 + len(beam) - 100
