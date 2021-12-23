from aoc20211223a import *


def aoc(data):
    data = data.split("\n")
    data = (
        "\n".join(data[:3])
        + """
  #D#C#B#A#
  #D#B#A#C#
"""
        + "\n".join(data[3:])
    )
    print(data)
    return game(parse(data), 0)
