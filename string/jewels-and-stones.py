from typing import Any


def solution(input: dict[str, Any]) -> int:
    jewels = input.get("jewels") or ""
    stones = input.get("stones") or ""
    total = 0
    stone_set = set[str]()
    for char in jewels:
        stone_set.add(char)
    for char in stones:
        if char in stone_set:
            total += 1
    return total
