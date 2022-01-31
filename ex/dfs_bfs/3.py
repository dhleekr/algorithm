di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    s, x, y = map(int, input().split())
    x -= 1
    y -= 1
    return n, k, grid, s, x, y

def find_idx(grid, k):
    res = []
    length = len(grid)
    for num in range(1, k+1):
        for i in range(length):
            for j in range(length):
                if grid[i][j] == num:
                    res.append([i, j])
    return res

def spread(grid, virus_idx):
    n = len(grid)
    new_virus = []
    while virus_idx:
        i, j = virus_idx.pop(0)
        num = grid[i][j]
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]

            if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 0:
                grid[new_i][new_j] = num
                new_virus.append([new_i, new_j])
    return grid, new_virus
n, k, grid, s, x, y = init()
virus_idx = find_idx(grid, k)

for _ in range(s):
    grid, virus_idx = spread(grid, virus_idx)

print(grid[x][y])