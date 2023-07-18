import sys
input = sys.stdin.readline

n = int(input())
queue = []
for i in range(n):
    func = input().split()
    if func[0] == "push":
        queue.append(func[1])
    elif func[0] == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif func[0] == "size":
        print(len(queue))
    elif func[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif func[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif func[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)