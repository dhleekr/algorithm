di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, grid

def get_idx(num):
    res = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == num:
                res.append([i, j])
    return res

def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combination(arr[i+1:], r - 1):
                yield [arr[i]] + j

def deepcopy(grid):
    new = []
    for i in range(len(grid)):
        new.append(grid[i][:])
    return new

def bfs(i, j):
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    q = [[i, j]]
    while q:
        i, j = q.pop(0)
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 0 and visited[new_i][new_j] == 0:
                q.append([new_i, new_j])
                visited[new_i][new_j] = 1
                grid[new_i][new_j] = 2
    

n, m, grid = init()
zero = get_idx(0)
virus = get_idx(2)

max_area = 0
for walls in combination(zero, 3):
    temp_grid = deepcopy(grid)
    for i, j in walls:
        grid[i][j] = 1
    for i, j in virus:
        bfs(i, j)
    max_area = max(max_area, len(get_idx(0)))
    grid = temp_grid

print(max_area)