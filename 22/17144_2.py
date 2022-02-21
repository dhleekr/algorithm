di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    r, c, t = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(r)]
    cleaner = []
    for i in range(r):
        if grid[i][0] == -1:
            cleaner.append([i, 0])
    return r, c, t, grid, cleaner

def find_idx():
    res = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] != 0 and grid[i][j] != -1:
                res.append([i, j])
    return res

def spread(dust_indices):
    temp = [row[:] for row in grid]
    for i, j in dust_indices:
        total = 0
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < r and 0 <= new_j < c and grid[new_i][new_j] != -1:
                grid[new_i][new_j] += temp[i][j] // 5
                total += temp[i][j] // 5
        grid[i][j] -= total

def air_clean():
    u, d = cleaner[0][0], cleaner[1][0]
    for i in range(u - 1, 0, -1):
        grid[i][0] = grid[i - 1][0]
        grid[i - 1][0] = 0
    for j in range(c - 1):
        grid[0][j] = grid[0][j + 1]
        grid[0][j + 1] = 0
    for i in range(u):
        grid[i][c - 1] = grid[i + 1][c - 1]
        grid[i + 1][c - 1] = 0
    for j in range(c - 1, 1, -1):
        grid[u][j] = grid[u][j - 1]
        grid[u][j - 1] = 0

    for i in range(d + 1, r - 1):
        grid[i][0] = grid[i + 1][0]
        grid[i + 1][0] = 0
    for j in range(c - 1):
        grid[r - 1][j] = grid[r - 1][j + 1]
        grid[r - 1][j + 1] = 0
    for i in range(r - 1, d, -1):
        grid[i][c - 1] = grid[i - 1][c - 1]
        grid[i - 1][c - 1] = 0
    for j in range(c - 1, 1, -1):
        grid[d][j] = grid[d][j - 1]
        grid[d][j - 1] = 0

r, c, t, grid, cleaner = init()
for _ in range(t):
    dust_indices = find_idx()
    spread(dust_indices)
    air_clean()

print(sum(sum(row) for row in grid) + 2)