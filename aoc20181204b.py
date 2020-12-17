from aoc20181204a import get_sleeps


def aoc(data):
    guards = get_sleeps(data)
    max = 0
    max_guard = None
    max_m = None
    for m in range(60):
        for guard in guards.keys():
            total = 0
            for time in guards[guard]:
                if time[0] <= m < time[1]:
                    total += 1
            if total > max:
                max = total
                max_guard = guard
                max_m = m
    return max_guard * max_m
