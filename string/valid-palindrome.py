import re


def solution(s: str) -> bool:
    regex = r"[a-z0-9]"
    matches = re.findall(regex, s.lower())
    length = len(matches)
    for i in range(0, length):
        if matches[i] != matches[length - i - 1]:
            return False
    return True
