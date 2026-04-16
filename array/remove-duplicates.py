"""
26. Remove Duplicates from Sorted Array

Approach: Two Pointer
Time Complexity: O(n)
Space Complexity: O(1)
"""


def solution(nums: list[int]) -> int:

    unique_elements = 0
    for i in range(len(nums)):
        if nums[unique_elements] != nums[i]:
            unique_elements += 1
            nums[unique_elements] = nums[i]
    return unique_elements + 1
