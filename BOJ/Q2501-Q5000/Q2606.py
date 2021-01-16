import heapq
import sys

n = int(input())
v = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
q = []

for _ in range(v):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

heapq.heappush(q, 1)
visited[1] = 1
ans = -1
while q :
    node = heapq.heappop(q)
    ans += 1
    for i in range(1, n+1):
        if graph[node][i] == 0 or visited[i] == 1 or i == node : continue
        visited[i] = 1
        heapq.heappush(q,i)
        
print(ans)