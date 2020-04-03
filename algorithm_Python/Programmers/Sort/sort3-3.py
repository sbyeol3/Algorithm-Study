def solution(citations):
    citations.sort()
    h = []
    l = len(citations)
    i = int(l/2) #2
    if citations[0]>=l : return l # add
    
    while(i):
        if citations[l-i]>= i:
            h.append(i)
            i += 1
        else : 
            i = 0
    if len(h) == 0 : return 0 
    h.sort()
    return h[-1]

# Success!

# print(solution([3, 0, 6, 1, 5]))
print(solution([20,19,18,1])) 
# print(solution([22,42])) 

