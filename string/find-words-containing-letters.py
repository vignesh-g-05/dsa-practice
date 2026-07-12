from typing import Any, List


def solution(input: dict[str, Any]) -> List[int]:
    print(input)
    words = input.get("words")
    x = input.get("x")
    output: List[int] = []
    for i in range(len(words)):
        if x in words[i]:
            output.append(i)
    return output
