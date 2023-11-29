def aoc(data):
    total = 0
    for l in data.split("\n"):
        v = 0
        for c in l:
            v *= 5
            v += {"1": 1, "2": 2, "0": 0, "-": -1, "=": -2}[c]
        total += v
    ans = ""
    t = 5**1000
    while 0 <= total / (t * 2) < 0.25:
        t //= 5
    while t != 0:
        best_v = 0
        best_t = total
        for v in [-2, -1, 0, 1, 2]:
            if abs(total - t * v) < abs(best_t):
                best_v = v
                best_t = total - t * v
        ans += {1: "1", 2: "2", 0: "0", -1: "-", -2: "="}[best_v]
        total = best_t
        t //= 5
    return ans
