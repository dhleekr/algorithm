def init():
    d, w, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(d)]
    return d, w, k, grid

def col_check(grid):
    for j in range(w):
        seq = 1
        for i in range(d - 1):
            if grid[i][j] == grid[i + 1][j]:
                seq += 1
                if seq == k:
                    break
            else:
                seq = 1
        if seq != k:
            return False
    return True

def dfs(cnt, depth, grid):
    global ans
    if cnt >= k:
        return
    if col_check(grid):
        ans = min(ans, cnt)
        return
    if depth == d:
        return

    for mode in modes:
        if mode == 0 or mode == 1:
            temp = grid[depth][:]
            grid[depth] = [mode] * w
            dfs(cnt + 1, depth + 1, grid)
            grid[depth] = temp
        else:
            dfs(cnt, depth + 1, grid)


T = int(input())
for i in range(1, T + 1):
    d, w, k, grid = init()
    ans = k
    modes = [-1, 0, 1]
    dfs(0, 0, grid)
    print(f'#{i} {ans}')