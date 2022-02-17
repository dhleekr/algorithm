di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

def init():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, grid

def make_tornado():
    i = n // 2
    j = n // 2
    s = 0
    cnt = 0
    res = []
    while (i !=0 or j != 0):
        if cnt % 2 == 0:
            s += 1
        for _ in range(s):
            i += di[cnt]
            j += dj[cnt]
            res.append([i, j, cnt])
            if i == 0 and j == 0:
                break
        cnt = (cnt + 1) % 4
    return res

def spread(i, j, d): # y의 좌표
    global ans
    move = 0
    if 0 <= i + 2 * di[d] <n and 0 <= j + 2 * dj[d] < n:
        move += int(grid[i][j] * 0.05)
        grid[i + 2 * di[d]][j + 2 * dj[d]] += int(grid[i][j] * 0.05)
    else:
        move += int(grid[i][j] * 0.05)
        ans += int(grid[i][j] * 0.05)

    if 0 <= i + di[d] + di[(d - 1) % 4] < n and 0 <= j + dj[d] + dj[(d - 1) % 4] < n:
        move += int(grid[i][j] * 0.1)
        grid[i + di[d] + di[(d - 1) % 4]][j + dj[d] + dj[(d - 1) % 4]] += int(grid[i][j] * 0.1)
    else:
        move += int(grid[i][j] * 0.1)
        ans += int(grid[i][j] * 0.1)
    
    if 0 <= i + di[(d - 1) % 4] < n and 0 <= j + dj[(d - 1) % 4] < n:
        move += int(grid[i][j] * 0.07)
        grid[i + di[(d - 1) % 4]][j + dj[(d - 1) % 4]] += int(grid[i][j] * 0.07)
    else:
        move += int(grid[i][j] * 0.07)
        ans += int(grid[i][j] * 0.07)
    
    if 0 <= i + 2 * di[(d - 1) % 4] < n and 0 <= j + 2 * dj[(d - 1) % 4] < n:
        move += int(grid[i][j] * 0.02)
        grid[i + 2 * di[(d - 1) % 4]][j + 2 * dj[(d - 1) % 4]] += int(grid[i][j] * 0.02)
    else:
        move += int(grid[i][j] * 0.02)
        ans += int(grid[i][j] * 0.02)

    if 0 <= i + di[(d + 2) % 4] + di[(d - 1) % 4] < n and 0 <=  j+ dj[(d + 2) % 4] + dj[(d - 1) % 4] < n:
        move += int(grid[i][j] * 0.01)
        grid[i + di[(d + 2) % 4] + di[(d - 1) % 4]][j+ dj[(d + 2) % 4] + dj[(d - 1) % 4]] += int(grid[i][j] * 0.01)
    else:
        move += int(grid[i][j] * 0.01)
        ans += int(grid[i][j] * 0.01)

    if 0 <= i + di[d] + di[(d + 1) % 4] < n and 0 <=  j+ dj[d] + dj[(d + 1) % 4] < n:
        move += int(grid[i][j] * 0.1)
        grid[i + di[d] + di[(d + 1) % 4]][j+ dj[d] + dj[(d + 1) % 4]] += int(grid[i][j] * 0.1)
    else:
        move += int(grid[i][j] * 0.1)
        ans += int(grid[i][j] * 0.1)

    if 0 <= i + di[(d + 1) % 4] < n and 0 <= j + dj[(d + 1) % 4] < n:
        move += int(grid[i][j] * 0.07)
        grid[i + di[(d + 1) % 4]][j + dj[(d + 1) % 4]] += int(grid[i][j] * 0.07)
    else:
        move += int(grid[i][j] * 0.07)
        ans += int(grid[i][j] * 0.07)
    
    if 0 <= i + 2 * di[(d + 1) % 4] < n and 0 <= j + 2 * dj[(d + 1) % 4] < n:
        move += int(grid[i][j] * 0.02)
        grid[i + 2 * di[(d + 1) % 4]][j + 2 * dj[(d + 1) % 4]] += int(grid[i][j] * 0.02)
    else:
        move += int(grid[i][j] * 0.02)
        ans += int(grid[i][j] * 0.02)

    if 0 <= i + di[(d + 2) % 4] + di[(d + 1) % 4] < n and 0 <=  j+ dj[(d + 2) % 4] + dj[(d + 1) % 4] < n:
        move += int(grid[i][j] * 0.01)
        grid[i + di[(d + 2) % 4] + di[(d + 1) % 4]][j+ dj[(d + 2) % 4] + dj[(d + 1) % 4]] += int(grid[i][j] * 0.01)
    else:
        move += int(grid[i][j] * 0.01)
        ans += int(grid[i][j] * 0.01)
    
    if 0 <= i + di[d] < n and 0 <= j + dj[d] < n:
        grid[i + di[d]][j + dj[d]] += grid[i][j] - move
    else:
        ans += grid[i][j] - move
    grid[i][j] = 0

n, grid = init()
tornado = make_tornado()
ans = 0
for i, j, d in tornado:
    spread(i, j, d)
print(ans)