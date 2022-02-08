total = [list(map(int, input().strip())) for _ in range(4)]
n = int(input())
cases = [list(map(int, input().split())) for _ in range(n)]

lrs = [[6, 2] for _ in range(4)]

for case in cases:
    gear, d = case
    gear -= 1
    rotation = [0, 0, 0, 0]
    rotation[gear] = d

    for i in range(gear, 3):
        if total[i][lrs[i][1]] == total[i + 1][lrs[i + 1][0]]:
            break
        else:
            rotation[i + 1] = -rotation[i]
    
    for j in range(gear, 0, -1):
        if total[j][lrs[j][0]] == total[j - 1][lrs[j - 1][1]]:
            break
        else:
            rotation[j - 1] = -rotation[j]

    for idx, d in enumerate(rotation):
        if d == 1:
            lrs[idx][0] = (lrs[idx][0] - 1) % 8
            lrs[idx][1] = (lrs[idx][1] - 1) % 8
        elif d == -1:
            lrs[idx][0] = (lrs[idx][0] + 1) % 8
            lrs[idx][1] = (lrs[idx][1] + 1) % 8

ans = 0
for idx, lr in enumerate(lrs):
    r = lr[1]
    if total[idx][(r - 2) % 8] == 1:
        ans += 2 ** idx

print(ans)