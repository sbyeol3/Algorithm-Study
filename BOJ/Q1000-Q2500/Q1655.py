import heapq
import sys

n = int(input())
maxH = []
minH = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(maxH) == len(minH) : heapq.heappush(maxH, -num)
    else : heapq.heappush(minH, num)
    
    if minH and -maxH[0] > minH[0]:
        maxT = heapq.heappop(maxH)
        minT = heapq.heappop(minH)
        heapq.heappush(maxH, -minT)
        heapq.heappush(minH, -maxT)

    print(-maxH[0])
