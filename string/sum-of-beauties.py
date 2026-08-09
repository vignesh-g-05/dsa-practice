from collections import defaultdict


def solution(s: str) -> int:
    length = len(s)
    sum_of_beauties = 0

    for i in range(length):
        freq: defaultdict[str, int] = defaultdict(int)

        for j in range(i, length):
            freq[s[j]] += 1

            min_freq = min(freq.values())
            max_freq = max(freq.values())

            sum_of_beauties += max_freq - min_freq

    return sum_of_beauties
