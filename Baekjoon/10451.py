import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = 1

    if not visited[graph[v]]:
        dfs(graph, graph[v], visited)

t = int(input())

for i in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().rstrip().split()))
    visited = [0] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)
    
    print(cnt)