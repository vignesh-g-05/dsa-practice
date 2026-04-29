def approach(x: int) -> int:
    if x < 10 and x > -10:
        return x
    sign = 1
    if x < 0:
        sign = -1

    num = sign * x
    rev = 0
    while num > 0:
        rev *= 10
        rev += num % 10
        num = num // 10

    max_range = 2**31 - 1
    min_range = -(2**31)
    ans = sign * rev

    if ans < min_range or ans > max_range:
        return 0

    return ans
