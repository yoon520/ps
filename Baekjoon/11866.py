from collections import deque
n, k = map(int, input().split())
q = deque([i+1 for i in range(n)])
res = []

while q:
    q.rotate(-(k-1))
    res.append(n.popleft())
    
print("<", end='')
print(*res, sep=', ', end='')
print(">")