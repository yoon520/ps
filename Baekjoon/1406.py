import sys
input = sys.stdin.readline

l, r = list(input().rstrip()), []
n = int(input())

for _ in range(n):
    func = list(input().split())

    if func[0] == 'L' and l:
        r.append(l.pop())
    elif func[0] == 'D' and r:
        l.append(r.pop())
    elif func[0] == 'B' and l:
        l.pop()
    elif func[0] == 'P':
        l.append(func[1])
        
print(''.join(l + r[::-1]))

