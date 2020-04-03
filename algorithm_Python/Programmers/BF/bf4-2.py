def solution(brown, red):
    for i in range(3,int(brown/2)+1):
        if (brown - i*2) %2 == 1 : continue
        innerWidth = (brown - i*2)/2
        if (i-2)*(innerWidth) != red : continue
        return [innerWidth+2, i]
    return 0

print(solution(10,2))
print(solution(8,1))
print(solution(16,9))