import sys

def vps(list):
    s = []
    for i in list:
        if i == "(":
            s.append(i)
        elif i == ")":
            if not s:
                return False
            s.pop()
    return len(s) == 0

n = int(sys.stdin.readline())

for _ in range(n):
    ps = list(sys.stdin.readline().rstrip())
    
    if vps(ps):
        print("YES")
    else:
        print("NO")