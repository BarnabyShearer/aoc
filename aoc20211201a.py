from collections import deque
from itertools import islice


def parse(data):
    return [int(l) for l in data.split()]


def window(data, n=2):
    yield (result := deque(islice(data := iter(data), n), maxlen=n))
    for e in data:
        result.append(e)
        yield result


def count_inc(data):
    return sum(cur > prev for prev, cur in window(data))


def aoc(data):
    return count_inc(parse(data))
