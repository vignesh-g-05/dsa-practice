class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict[int, int](int)

        for n in nums:
            freq_map[n] += 1

        sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        result = list[int]()

        for i in range(k):
            result.append(sorted_freq[i][0])

        return result
