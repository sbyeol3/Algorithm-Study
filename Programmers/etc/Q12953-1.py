def solution(arr):
    def gcd(a,b):
        if a % b == 0: return b
        else: return gcd(b,a%b)
    lcs = 1
    for i in arr :
        lcs = (lcs * i) / gcd(lcs,i)
    return lcs

print(solution([2,6,8,14]))