class Solution:

    def encode(self, strs: list[str]) -> str:
        return str(strs)

    def decode(self, s: str) -> list[str]:
        return ast.literal_eval(s)