def solution(baseball):
    baseballSort = sorted(baseball, key=lambda x:x[1], reverse=True)
    candidate = []
    
    for hint in baseballSort :
        num, s, b = hint
        num = list(num)
        if s == 3 : return 1
        elif s == 2 :
            for i in range(3) :
                
        elif s == 1 :
    
    return len(candidate)