n, k = map(int, input().split())
s = list(map(int, input()))
stack = []

for i in s:
    while stack and stack[-1]<i and k > 0:
        stack.pop()
        k -= 1
    stack.append(i)

while k != 0:
    stack.pop()
    k -= 1

print(*stack, sep='')