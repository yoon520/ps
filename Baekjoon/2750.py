arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
arr.sort()
print(*arr, sep='\n')