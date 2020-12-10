from aoc20201209a import parse, aoc as a


def aoc(data):
    target = a(data)
    nums = parse(data)
    for i in range(len(nums)):
        for ii in range(len(nums) - i):
            if sum(nums[i : i + ii]) == target:
                return min(nums[i : i + ii]) + max(nums[i : i + ii])
