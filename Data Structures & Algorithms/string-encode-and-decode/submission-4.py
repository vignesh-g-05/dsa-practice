class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "#" + s

        return encoded_string

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