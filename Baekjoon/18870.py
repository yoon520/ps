import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().rstrip().split()))
x2 = sorted(set(x))
idx = {}

for i in range(len(x2)):
    idx[x2[i]] = i

for i in x:
    print(idx[i], end=' ')