class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict[str, list[str]]()

        for s in strs:
            key = str(sorted(s))

            if key in groups:
                groups[key].append(s)
                continue

            groups[key] = [s]

        return list(groups.values())