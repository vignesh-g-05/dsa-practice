def solution(strs: list[str]) -> list[list[str]]:
    groups = dict[str, list[str]]()

    for s in strs:
        group_key: str = "".join(sorted(s))

        existing = groups.get(group_key)

        if existing is None:
            groups[group_key] = [s]
        else:
            groups[group_key].append(s)

    return list(groups.values())
