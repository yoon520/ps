import sys
input = sys.stdin.readline

def dfs(start):
    global cnt
    visited[start] = 1
    cnt += 1

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0

for _ in range(m):
    v1, v2 = map(int, input().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)
print(cnt-1)