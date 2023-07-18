import sys

stack = []
t = int(sys.stdin.readline())

for _ in range(t):
    func = sys.stdin.readline().split()
    if func[0] == "push":
        stack.append(func[1])
    elif func[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif func[0] == "size":
        print(len(stack))
    elif func[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif func[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])

