"""
136. Single Number

Approach:
Time: O(n)
Space: O(n)
"""


def approach(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    map: dict[int, int] = dict()

    for i in range(n):
        curr = nums[i]
        existing = map.get(curr)
        if existing is None:
            map[curr] = True
        else:
            map.pop(curr)
    keys = list(map.keys())
    return keys[0]
