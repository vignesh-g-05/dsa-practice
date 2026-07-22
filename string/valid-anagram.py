def solution(strs: str) -> bool:
    s = strs[0]
    t = strs[1]

    if len(s) != len(t):
        return False
    if s == t:
        return True

    map_s = dict[str, int]()
    map_t = dict[str, int]()

    for i in range(len(s)):
        curr_s = s[i]
        curr_t = t[i]

        map_s[curr_s] = map_s.get(curr_s, 0) + 1
        map_t[curr_t] = map_t.get(curr_t, 0) + 1

    for key in map_s.keys():
        curr_s = map_s.get(key)
        curr_t = map_t.get(key)

        if curr_s != curr_t:
            return False
    return True
