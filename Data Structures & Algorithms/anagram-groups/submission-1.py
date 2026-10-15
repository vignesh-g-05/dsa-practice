class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict[tuple[int, ...], list[str]](list)

        for s in strs:
            char_counts = [0] * 26
            for c in s:
                char_counts[ord(c) - ord("a")] += 1

            grouped_anagrams[tuple(char_counts)].append(s)

        return list(grouped_anagrams.values())