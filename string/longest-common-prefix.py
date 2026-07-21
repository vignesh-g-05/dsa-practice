def solution(strs: str) -> str:
    x = 0
    first_word = strs[0]

    if not first_word:
        return ""
    while x < len(first_word):
        curr_char = first_word[x]
        for word in strs:
            print(word, curr_char, len(word), x)
            if len(word) == x or word[x] != curr_char:
                return first_word[:x]
        x += 1
    return first_word[:x]
