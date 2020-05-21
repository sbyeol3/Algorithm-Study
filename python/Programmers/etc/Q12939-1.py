def solution(s):
    params = list(map(int,s.split(" ")))
    return str(min(params)) + " " + str(max(params))


print(solution("-1 -2 -3 -4"))
print(solution("1 2 3 4"))
print(solution("-1 -1"))