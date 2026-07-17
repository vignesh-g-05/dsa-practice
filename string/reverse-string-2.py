from typing import Any


def solution(input: dict[str, Any]) -> str:
    s: str = input.get("s", "")
    k: int = input.get("k", 0)
    length = len(s)
    output = ""
    substr = ""
    is_rev = False
    for i in range(length):
        if i % k == 0:
            output += substr
            substr = ""
            is_rev = not is_rev
        c = s[i]
        if is_rev:
            substr = c + substr
        else:
            substr = substr + c

    output += substr

    return output
