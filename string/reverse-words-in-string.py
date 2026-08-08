def solution1(s: str) -> str:
    rev = ""
    curr_word = ""
    for c in s:
        if c == " " and curr_word == "":
            continue

        if c != " ":
            curr_word += c
            continue

        if rev != "":
            curr_word += " "

        rev = curr_word + rev
        curr_word = ""

    if curr_word != "" and rev != "":
        curr_word += " "

    return curr_word + rev


def solution2(s: str) -> str:
    return " ".join(s.split()[::-1])
