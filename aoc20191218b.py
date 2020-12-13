from aoc20191218a import search


def aoc(data):
    w = data.index("\n") + 1
    pos = data.index("@")
    data = data[: pos - w - 1] + "@#@" + data[pos - w + 2 :]
    data = data[: pos - 1] + "###" + data[pos + 2 :]
    data = data[: pos + w - 1] + "@#@" + data[pos + w + 2 :]
    return search(data)
