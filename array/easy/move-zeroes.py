"""
283. Move Zeroes
Approach:
Two Pointer
Time: O(n)
Space: O(1)
"""


def solution(nums: list[int]) -> list[int]:
    ptr = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[ptr]
            nums[ptr] = nums[i]
            nums[i] = temp
            ptr += 1
    return nums
