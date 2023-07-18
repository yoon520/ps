bar = input()
s = []
cnt = 0

for i in range(len(bar)):
    if bar[i] == "(":
        s.append(bar[i])
    else:
        if bar[i-1] == "(":
            s.pop()
            cnt += len(s)
        else:
            s.pop()
            cnt += 1

print(cnt)