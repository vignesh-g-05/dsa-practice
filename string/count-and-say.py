def recursion(n: int) -> str:
    # base case
    if n == 1:
        return "1"

    rle_str = recursion(n - 1)

    compressed_str: str = ""
    curr_digit: str = rle_str[0]
    digit_count: int = 1
    for i in range(1, len(rle_str)):
        c = rle_str[i]

        if c == curr_digit:
            digit_count += 1
            continue

        compressed_str += str(digit_count) + curr_digit
        curr_digit = c
        digit_count = 1

    compressed_str += str(digit_count) + curr_digit

    return compressed_str
