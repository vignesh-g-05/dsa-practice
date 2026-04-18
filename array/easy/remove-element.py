"""
27. Remove Element

Approach: Two Pointer
Time: O(n)
Space: O(1)
"""


def solution(nums: list[int], val: int):
    x = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[x] = nums[i]
            x += 1

    return x
