import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(s):
    for i in t[s]:
        # 부모 노드를 모르면
        if not v[i]:
            # 부모 노드 저장
            v[i] = s
            dfs(i)

n = int(input())
t = [[] for _ in range(n+1)]
v = [0] * (n+1)

for _ in range(n-1):
    v1, v2 = map(int, input().rstrip().split())
    t[v1].append(v2)
    t[v2].append(v1)

dfs(1)

for i in range(2, n+1):
    print(v[i])