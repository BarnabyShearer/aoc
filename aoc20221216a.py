from collections import defaultdict
from aoc20191206b import dijkstra


def parse(data):
    return {
        k: (int(rate[5:-1]), tuple(i[:2] for i in p))
        for l in data.split("\n")
        for valve, k, has, flow, rate, tunnels, lead, to, valves, *p in [l.split(" ")]
    }


def prep(data):
    taps = {k for k in data.keys() if data[k][0]}
    return (
        data,
        taps,
        {
            (s, e): len(dijkstra({k: v[1] for k, v in data.items()}, s, e))
            for s in taps
            | {
                "AA",
            }
            for e in taps
            if s != e
        },
    )


def solve(data, taps, route, t=30):
    open = [(t, "AA", frozenset(), 0, 0)]
    all = defaultdict(lambda: 0)
    while open:
        t, p, seen, pr, pt = open.pop()
        all[seen] = max(all[seen], pt + pr * t)
        for d in taps - seen:
            dist = route[(p, d)]
            if t - dist > 0:
                open.append(
                    (
                        t - dist,
                        d,
                        seen
                        | {
                            d,
                        },
                        pr + data[d][0],
                        pt + pr * dist,
                    )
                )
    return all


def aoc(data):
    return max(solve(*prep(parse(data))).values())
