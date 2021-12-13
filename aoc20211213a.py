def parse(data):
    dots, folds = (s.split("\n") for s in data.split("\n\n"))
    dots = set((int(c) for c in x.split(",")) for x in dots)
    ifolds = []
    for fold in folds:
        match fold.split("="):
            case "fold along x", x:
                ifolds.append((int(x), 999))
            case "fold along y", y:
                ifolds.append((999, int(y)))
    return dots, ifolds


def fold(dots, fx, fy):
    return set(
        (2 * fx - x if x > fx else x, 2 * fy - y if y > fy else y) for x, y in dots
    )


def aoc(data):
    dots, folds = parse(data)
    dots = fold(dots, *folds[0])
    return len(dots)
