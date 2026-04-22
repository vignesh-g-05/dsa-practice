"""
485. Max Consecutive Ones

Approach:
Two Pointer
Time: O(n)
Space: O(1)
"""


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_count = 0
    count = 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0

    return max(max_count, count)
