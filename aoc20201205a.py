def seats(data):
    for seat in data.split("\n"):
        row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
        col = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
        yield row * 8 + col


def aoc(data):
    return max(seats(data))
