from collections import defaultdict


def solution(s: str) -> str:
    freq: defaultdict[str, int] = defaultdict(int)  # S[O(k)]
    organized: list[str] = []
    prev_char = ""

    for c in s:
        freq[c] += 1

    while bool(freq):
        k = get_max_freq_char(freq, prev_char)

        if k is None:
            return ""
        prev_char = k
        organized.append(k)
        cnt = freq.get(k, 0)

        if cnt == 1:
            freq.pop(k)
        else:
            freq[k] -= 1

    return "".join(organized)


def get_max_freq_char(freq: dict[str, int], excluded: str) -> str | None:
    max_freq: int = 0
    max_char: str = ""

    for k in freq:
        if k == excluded:
            continue

        cnt = freq.get(k, 0)

        if cnt < max_freq:
            continue

        max_freq = cnt
        max_char = k

    return max_char or None
