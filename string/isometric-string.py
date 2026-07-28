def solution(strs: list[str]) -> bool:
    s = strs[0]
    t = strs[1]

    if len(s) != len(t):
        return False
    if s == t:
        return True

    map_s_to_t = dict[str, str]()
    map_t_to_s = dict[str, str]()

    for i in range(len(s)):
        mapped_s = map_s_to_t.get(s[i])
        mapped_t = map_t_to_s.get(t[i])

        if mapped_s is None:
            map_s_to_t[s[i]] = t[i]
        elif mapped_s != t[i]:
            return False

        if mapped_t is None:
            map_t_to_s[t[i]] = s[i]
        elif mapped_t != s[i]:
            return False

    return True
