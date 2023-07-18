import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([])

for i in range(n):
    func = input().split()
    if func[0] == "push":
        q.append(func[1])
    elif func[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif func[0] == "size":
        print(len(q))
    elif func[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif func[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif func[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)