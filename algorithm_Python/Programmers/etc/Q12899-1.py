def solution(n):
    num = ['1','2','4']
    division = []
    if n < 4 : return num[n%3-1]
    while(n>3):
        r = n % 3
        division.append(r)
        n = int(n/3)
        if n<4 : division.append(n)
    
    answer = ''
    while(division):
        d = division.pop()
        answer += num[d-1]

    return answer

print(solution(4))