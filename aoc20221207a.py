from collections import defaultdict


def parse(data):
    stack = ()
    dirs = defaultdict(lambda: 0)
    for line in data.split("\n"):
        match line.split():
            case ("$", "cd", "/"):
                stack = ("/",)
            case ("$", "cd", ".."):
                stack = stack[:-1]
            case ("$", "cd", d):
                stack += (d,)
            case ("$", "ls"):
                pass
            case ("dir", n):
                pass
            case (s, n):
                for i in range(len(stack)):
                    dirs[stack[: i + 1]] += int(s)
    return dirs


def aoc(data):
    return sum(s for s in parse(data).values() if s <= 100000)
