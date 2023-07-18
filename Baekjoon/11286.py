import heapq, sys
input=sys.stdin.readline

n = int(input())
h = []

for i in range(n):
    k = int(input())
    if k == 0:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
    else:
        heapq.heappush(h,(abs(k),k))
