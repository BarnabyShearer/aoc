from aoc20231215a import *


def aoc(data):
    boxes = [{} for _ in range(256)]
    for l in data.split(","):
        if "=" in l:
            lab, v = l.split("=")
            boxes[hash(lab)][lab] = int(v)
        else:
            lab, _ = l.split("-")
            if lab in boxes[hash(lab)]:
                del boxes[hash(lab)][lab]
    total = 0
    for bi, box in enumerate(boxes, 1):
        for li, l in enumerate(box.values(), 1):
            total += bi * li * l
    return total
