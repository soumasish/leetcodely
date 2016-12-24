"""Given an array of integers, return indices of the two numbers such that they add up to a
    specific target.You may assume that each input would have exactly one solution."""


def two_sum(nums, target):

    map = {}

    for i, v in enumerate(nums):
        diff = target - v
        if diff in map:
            return [map[diff], i]
        else:
            map[v] = i