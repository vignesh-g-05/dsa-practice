class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = defaultdict[str, int](int)
        t_chars = defaultdict[str, int](int)

        for s_char, t_char in zip(s, t):
            s_chars[s_char] += 1
            t_chars[t_char] += 1

        for key in s_chars:
            s_char = s_chars.get(key)
            t_char = t_chars.get(key)
            if s_char != t_char:
                return False

        return True
