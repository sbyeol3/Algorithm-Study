def solution(n):
    if n == 1 : return 4
    end = int(n ** 1/2) + 1
    for i in range(2,end) :
        if i ** 2 == n : return (i+1) ** 2
    return -1