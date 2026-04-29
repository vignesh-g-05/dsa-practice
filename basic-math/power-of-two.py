def approach(n: int) -> bool:
    if n < 3:
        return True
    if n % 2 == 1:
        return False
    i = 2
    while True:
        val = 2**i
        if val == n:
            return True
        if val > n:
            return False
        i += 1
