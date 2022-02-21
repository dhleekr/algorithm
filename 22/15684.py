def init():
    n, m, h = map(int, input().split())
    a = [[0] * n for _ in range(h)]
    for _ in range(m):
        i, j = map(int, input().split())
        a[i-1][j-1] = 1
    return n, m, h,a

def move():
    for j in range(n):
        num = j
        for i in range(h):
            if a[i][num]:
                num += 1
            elif a[i][num - 1]:
                num -= 1
        if j != num:
            return False
    return True

def dfs(cnt, idx, r):
    global ans
    if cnt == r:
        if move():
            ans = cnt
        return

    for i in range(idx, h):
        for j in range(n-1):
            if a[i][j]:
                continue
            if j - 1 >= 0 and a[i][j-1]:
                continue
            if j + 1 < n and a[i][j+1]:
                continue
            a[i][j] = 1
            dfs(cnt + 1, i, r)
            a[i][j] = 0

n, m, h, a = init()

ans, flag = 1e10, 1
for r in range(4):
    dfs(0, 0, r)
    if ans != 1e10:
        print(ans)
        flag = 0
        break
if flag:
    print(-1)