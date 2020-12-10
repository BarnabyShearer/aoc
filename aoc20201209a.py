def parse(data):
    return [int(line) for line in data.split("\n")]


def match(target, list):
    return any([a != b and a + b == target for a in list for b in list])


def aoc(data):
    nums = parse(data)
    for i in range(len(nums) - 25):
        if not match(nums[i + 25], nums[i : i + 25]):
            return nums[i + 25]
