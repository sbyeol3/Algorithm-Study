def solution(n):
    cnt = 0
    while(n):
        if n % 2 == 0 : n /= 2
        else :
            n -= 1
            cnt += 1
    return cnt

print(solution(5000))