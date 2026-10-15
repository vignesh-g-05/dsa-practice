class Solution:

    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""

        string_sizes: list[str] = []

        for s in strs:
            string_sizes.append(str(len(s)))
            string_sizes.append("#")
            string_sizes.append(s)

        return "".join(string_sizes)

    def decode(self, s: str) -> list[str]:
        decoded_list: list[str] = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            decoded_list.append(s[j + 1 : count + j + 1])
            i = j + 1 + count

        return decoded_list