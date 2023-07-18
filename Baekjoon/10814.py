import sys

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2][0]
    left, right, equal = [], [], []

    for i in arr:
        if pivot > i[0]:
            left.append(i)
        elif pivot < i[0]:
            right.append(i)
        else:
            equal.append(i)
    
    return quicksort(left) + equal + quicksort(right)


n = int(sys.stdin.readline())
members = []
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    members.append([int(a), b])

for i in quicksort(members):
    print(*i)