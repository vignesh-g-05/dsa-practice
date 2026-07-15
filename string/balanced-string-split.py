def solution(s: str) -> int:
    l_cnt = r_cnt = 0
    pairs = 0
    for c in s:
        if c == "R":
            r_cnt += 1
        else:
            l_cnt += 1
        if l_cnt == r_cnt:
            pairs += 1
            l_cnt = r_cnt = 0
    return pairs
