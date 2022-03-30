di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, m, t = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    airs = []
    for i in range(n):
        if grid[i][0] == -1:
            airs.append([i, 0])
            airs.append([i + 1, 0])
            break
    return n, m, t, grid, airs

def deepcopy(grid):
    return [row[:] for row in grid]

def spread():
    new = deepcopy(grid)
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                cnt = 0
                for d in range(4):
                    new_i = i + di[d]
                    new_j = j + dj[d]
                    if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] != -1:
                        new[new_i][new_j] += grid[i][j] // 5
                        cnt += 1
                new[i][j] -= (grid[i][j] // 5) * cnt
    return new

def clean():
    u, d = airs[0][0], airs[1][0]
    for i in range(u - 1, 0, -1):
        grid[i][0] = grid[i - 1][0]
        grid[i - 1][0] = 0
    for j in range(m - 1):
        grid[0][j] = grid[0][j + 1]
        grid[0][j + 1] = 0
    for i in range(u):
        grid[i][m - 1] = grid[i + 1][m - 1]
        grid[i + 1][m - 1] = 0
    for j in range(m - 1, 1, -1):
        grid[u][j] = grid[u][j - 1]
        grid[u][j - 1] = 0

    for i in range(d + 1, n - 1):
        grid[i][0] = grid[i + 1][0]
        grid[i + 1][0] = 0
    for j in range(m - 1):
        grid[n - 1][j] = grid[n - 1][j + 1]
        grid[n - 1][j + 1] = 0
    for i in range(n - 1, d, -1):
        grid[i][m - 1] = grid[i - 1][m - 1]
        grid[i - 1][m - 1] = 0
    for j in range(m - 1, 1, -1):
        grid[d][j] = grid[d][j - 1]
        grid[d][j - 1] = 0


n, m, t, grid, airs = init()

for _ in range(t):
    grid = spread()
    clean()
print(sum(sum(row) for row in grid) + 2)