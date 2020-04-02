def solution(brown, red):
    for i in range(int(brown/4),int(brown/2)+1):
        if (brown - i*2) %2 == 1 : continue
        innerHeight = (brown - i*2)/2
        if (i-2)*(innerHeight) != red : continue
        return [innerHeight+2, i]
    return 0

print(solution(10,2))
print(solution(8,1))
print(solution(16,9))

# 4,5,6,7,9,10