from collections import defaultdict
from math import ceil


def priority_queue(s: str) -> str:
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


def odd_even(s: str) -> str:
    # find frequency and max freq
    freq: defaultdict[str, int] = defaultdict(int)
    max_freq: int = 0
    n: int = len(s)

    for c in s:
        freq[c] += 1
        max_freq = max(max_freq, freq[c])

    # return if max freq is more than half
    if max_freq > ceil(n / 2):
        return ""

    # sort dict by frequency
    sorted_freq: dict[str, int] = dict(
        sorted(freq.items(), key=lambda item: item[1], reverse=True)
    )

    organized: list[str] = [""] * n

    even_ptr: int = 0
    odd_ptr: int = 1
    for k, v in sorted_freq.items():
        for _ in range(v):
            if even_ptr < n:
                organized[even_ptr] = k
                even_ptr += 2
            elif odd_ptr < n:
                organized[odd_ptr] = k
                odd_ptr += 2

    return "".join(organized)
