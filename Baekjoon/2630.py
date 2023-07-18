import sys
input = sys.stdin.readline
white, blue = 0, 0

def cut(n, arr):
    global white, blue

    if all('1' not in i for i in arr):
        white += 1
        return
    elif all('0' not in i for i in arr):
        blue += 1
        return
    
    n //= 2
    cut(n, [i[:n] for i in arr[:n]])
    cut(n, [i[n:] for i in arr[:n]])
    cut(n, [i[:n] for i in arr[n:]])
    cut(n, [i[n:] for i in arr[n:]])

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input().rstrip().split()))

cut(n, arr)
print(white, blue, sep= '\n')