n = int(input())
arr = []
for _ in range(n):
    total = 0
    s = input()
    for i in s:
        if i.isdigit():
            total += int(i)
    arr.append([s, len(s), total])

arr = sorted(arr, key = lambda x: (x[1], x[2], x[0]))

for i in arr:
    print(i[0])