import heapq, sys
input = sys.stdin.readline

h = []
n = int(input())

for i in range(n):
    k = int(input())
    if k == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, k)