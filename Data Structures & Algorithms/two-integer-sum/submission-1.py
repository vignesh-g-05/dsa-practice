class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = dict[int, tuple[int, int]]()

        for i, num in enumerate(nums):
            if num in diff_map:
                return [diff_map.get(num, [])[0], i]
            diff_map[target - num] = (i, num)

        return []
