def solution(words):
    cnt = 0
    for w in words :
        for i in range(len(w)-1,0,-1):
            has = False
            for j in words :
                if j.find(w[:i]) == 0 : has = True
            if has : 
                print(i)
                cnt += i
                break
    return cnt

print(solution(['go','gone','guild']))