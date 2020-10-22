def solution(n):
    base3 = ''
    while(True):
        q, r = divmod(n, 3)
        n = q
        base3 = str(r) + base3
        if q == 0 : break
    reversedBase3 = list(reversed(list(base3)))
    length = len(reversedBase3)
    decimal = 0
    for i, digit in enumerate(reversedBase3) :
        decimal += int(digit) * (3 ** (length - i - 1))
    return decimal