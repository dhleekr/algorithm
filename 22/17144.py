di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    r, c, t = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(r)]
    return r, c, t, grid

def find_idx(grid):
    dust = []
    air = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] == -1:
                air.append([i, j])
            elif grid[i][j] != 0:
                dust.append([i, j])
    return air, dust

def spread(grid, dust):
    new_grid = [[0] * c for _ in range(r)]
    for i, j in air:
        new_grid[i][j] = -1
    for i, j in dust:
        spread_amount = grid[i][j] // 5
        cnt = 0
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < r and 0 <= new_j < c and grid[new_i][new_j] != -1:
                cnt += 1
                new_grid[new_i][new_j] += spread_amount
        new_grid[i][j] += grid[i][j] - (cnt * spread_amount)
    return new_grid

def air_clean(grid):
    for idx, a in enumerate(air):
        ai, _ = a
        if idx == 0:
            for i in range(ai - 1, -1, -1):
                if grid[i + 1][0] == -1:
                    grid[i][0] = 0
                else:
                    grid[i + 1][0] = grid[i][0]
                    grid[i][0] = 0
            for j in range(1, c):
                grid[0][j - 1] = grid[0][j]
                grid[0][j] = 0
            for i in range(1, ai + 1):
                grid[i - 1][c - 1] = grid[i][c - 1]
                grid[i][c - 1] = 0
            for j in range(c - 2, 0, -1):
                grid[ai][j + 1] = grid[ai][j]
                grid[ai][j] = 0
        else:
            for i in range(ai + 1, r):
                if grid[i - 1][0] == -1:
                    grid[i][0] = 0
                else:
                    grid[i - 1][0] = grid[i][0]
                    grid[i][0] = 0
            for j in range(1, c):
                grid[r - 1][j - 1] = grid[r - 1][j]
                grid[r - 1][j] = 0
            for i in range(r - 2, ai - 1, -1):
                grid[i + 1][c - 1] = grid[i][c - 1]
                grid[i][c - 1] = 0
            for j in range(c - 2, 0, -1):
                grid[ai][j + 1] = grid[ai][j]
                grid[ai][j] = 0

r ,c ,t, grid = init()

for _ in range(t):
    air, dust = find_idx(grid)
    grid = spread(grid, dust)
    grid = air_clean(grid)

print(sum(sum(row) for row in grid) + 2)