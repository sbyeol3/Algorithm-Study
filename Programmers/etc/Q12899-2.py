def solution(n):
    if n < 4 : return '124'[n-1]
    division = []
    while(n>3):
        q,r = divmod(n-1,3)
        n = q
        division.append(r)
        if n <= 3 : division.append(n-1)
    
    answer = ''
    while(division):
        d = division.pop()
        answer += '124'[d]

    return answer

print(solution(13) == '111')
print(solution(11) == '42')
print(solution(16) == '121')
print(solution(19) == '141', solution(19))
print(solution(500000000) == '421211211121241112')