from aoc20221207a import *


def aoc(data, total=70000000, need=30000000):
    dirs = parse(data)
    return min(s for s in dirs.values() if s >= need - (total - dirs[("/",)]))
