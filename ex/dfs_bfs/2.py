di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def index(grid, num):
    row = len(grid)
    col = len(grid[0])
    res = []
    for i in range(row):
        for j in range(col):
            if grid[i][j] == num:
                res.append([i, j])
    return res

def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for j in combination(array[i+1:], r-1):
                yield [array[i]] + j

def deepcopy(grid):
    new_grid = []
    for i in range(n):
        new_grid.append(grid[i][:])
    return new_grid


n, m = map(int, input().split())
original_grid = [list(map(int, input().split())) for _ in range(n)]

empty = index(original_grid, 0)
max_area = 0
for idx in combination(empty, 3):
    virus = index(original_grid, 2)
    grid = deepcopy(original_grid)
    visited = [[0]*m for _ in range(n)]
    for i, j in idx:
        grid[i][j] = 1
    
    while virus:
        i, j = virus.pop(0)
        visited[i][j] = 1
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < n and 0 <= new_j < m and not visited[new_i][new_j] and grid[new_i][new_j] == 0:
                virus.append([new_i, new_j])
                visited[new_i][new_j] = 1
                grid[new_i][new_j] = 2

    max_area = max(max_area, len(index(grid, 0)))

print(max_area)