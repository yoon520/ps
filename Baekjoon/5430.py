from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    func = input().rstrip()
    k = int(input())
    l = deque(input()[1:-2].split(','))
    if k == 0:
        l = deque([])
    
    check = 0
    reverseFlag = 0

    for i in func:
        if i == 'R':
            reverseFlag = (reverseFlag + 1) % 2
        elif i == 'D':
            try:
                if reverseFlag == 0:
                    l.popleft()
                elif reverseFlag == 1:
                    l.pop()
            except:
                print("error")
                check = 1
                break
    if check == 0:
        if reverseFlag == 1:
            l.reverse()
        print('[', end='')
        print(*l, sep=',', end='')
        print(']')
