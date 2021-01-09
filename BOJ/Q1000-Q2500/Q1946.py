import sys

t = int(input())
result = []

for _ in range(t):
    num = int(input())
    scores = sorted([list(map(int, sys.stdin.readline().strip().split())) for x in range(num)],
                   key = lambda x: x[0])    
    cnt = 0
    min_interview = 100001
    
    for i in range(num):
        interview = scores[i][1]
        if interview < min_interview :
            min_interview = interview
            cnt += 1
    result.append(cnt)

for i in range(t):
    print(result[i])