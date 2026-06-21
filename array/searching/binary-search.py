from typing import Any


def solution(input: dict[str, Any]) -> int:
    nums: list[int] = input.get("nums", [])
    target: int = input.get("target", 0)
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_element = nums[mid]

        if mid_element < target:
            start = mid + 1
        elif mid_element > target:
            end = mid - 1
        else:
            return mid

    return -1
