import math
def solution(n,a,b):
    x, y = min(a,b), max(a,b)
    if x % 2 == 1 and y - x == 1 : return 1
    cnt = 1
    while(True) :
        x = math.ceil(x / 2)
        y = math.ceil(y / 2)
        cnt += 1
        if x % 2 == 1 and y - x == 1 : return cnt
    return cnt

print(solution(8,4,7)) # 3