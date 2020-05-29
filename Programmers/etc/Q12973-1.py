def solution(s):
    s = list(s)
    if len(s) % 2 != 0 : return 0
    while(s) :
        isPossible = False
        for i in range(1,len(s)) :
            if s[i] == s[i-1] :
                s = s[:i-1] + s[i+1:]
                isPossible = True
                break
        if not isPossible : return 0
    return 1
            
print(solution('baba'))
