dp = {}

def w(a, b, c):
    if (a, b, c) in dp : return dp[(a,b,c)]
    
    if a <= 0 or b <= 0 or c <= 0:
        dp[(a,b,c)] = 1
        return 1
    if a > 20 or b > 20 or c > 20 : return w(20, 20, 20)
    if a < b and b < c :
        val = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        dp[(a,b,c)] = val
        return val
    else :
        val = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        dp[(a,b,c)] = val
        return val
    
a, b, c = map(int, input().split())
while a != -1 or b != -1 or c != -1 :
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
    a, b, c = map(int, input().split())
