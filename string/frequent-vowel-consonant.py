def solution(s: str) -> int:
    char_map = dict[str, int]()
    max_vowels = 0
    max_consonants = 0
    VOWELS = "aeiou"
    for char in s:
        if char in VOWELS:
            count = char_map.get(char, 0) + 1
            char_map[char] = count
            max_vowels = max(count, max_vowels)
        else:
            count = char_map.get(char, 0) + 1
            char_map[char] = count
            max_consonants = max(count, max_consonants)

    return max_vowels + max_consonants
