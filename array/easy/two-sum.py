def solution(nums: list[int], target: int) -> list[int]:
    diff_map = {}

    for i, num in enumerate(nums):
        if num in diff_map:
            return [diff_map[num], i]

        diff_map[target - num] = i

    return []
