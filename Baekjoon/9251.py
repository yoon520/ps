str1 = input()
str2 = input()
lcs = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]

for i, alpha1 in enumerate(str2, start=1):
    for j, alpha2 in enumerate(str1, start=1):
        if alpha1 == alpha2:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[-1][-1])