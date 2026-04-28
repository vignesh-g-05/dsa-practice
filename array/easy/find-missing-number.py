"""
268. Missing Number

Approach1:
Time: O(n)
Space: O(1)

Approach2:
Time: O(n)
Space: O(1)
"""


def approach1(nums: list[int]) -> int:
    for i in range(len(nums)):
        if i not in nums:
            return i
    return len(nums)


def approach2(nums: list[int]) -> int:
    n = len(nums)
    total_sum = (n * (n + 1)) // 2
    sum_of_array = 0

    for i in range(n):
        sum_of_array += nums[i]

    return total_sum - sum_of_array
