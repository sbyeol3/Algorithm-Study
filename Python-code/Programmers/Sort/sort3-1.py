def solution(citations):
    citations.sort()
    h = []
    l = len(citations)
    i = int(l/2) #2
    
    while(i):
        if citations[l-i]>= i:
            h.append(i)
            i += 1
        else : i -= i

    h.sort()
    return h[-1]

# 9 16 fail

print(solution([3, 0, 6, 1, 5]))
print(solution([20,19,18,1])) 

