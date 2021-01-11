from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)] 
dfs_visited = [0] * (N+1)
bfs_visited = [0] * (N+1)

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

    
def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end = ' ')
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

dfs(graph, V, dfs_visited)
print()
bfs(graph, V, bfs_visited)