di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, grid

def deepcopy(grid):
    new_grid = []
    for i in range(n):
        new_grid.append(grid[i][:])
    return new_grid

def move(i, j, d, visited):
    new_i = i + di[d]
    new_j = j + dj[d]
    if 0 <= new_i < n and 0 <= new_j < n:
        if grid[new_i][new_j] == 0:
            grid[new_i][new_j] = grid[i][j]
            grid[i][j] = 0
            move(new_i, new_j, d, visited) 
        elif grid[new_i][new_j] == grid[i][j]:
            if visited[new_i][new_j] == 0:
                visited[new_i][new_j] = 1
                grid[new_i][new_j] *= 2
                grid[i][j] = 0

def dfs(depth):
    global max_score, grid

    if depth == 5:
        max_score = max(max(max(row) for row in grid), max_score)
        return

    for d in range(4):
        temp = deepcopy(grid)
        if d == 0:
            visited = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n - 1, -1, -1):
                    if grid[i][j] != 0:
                        move(i, j, d, visited)
        elif d == 1:
            visited = [[0] * n for _ in range(n)]
            for i in range(n - 1, -1, -1):
                for j in range(n):
                    if grid[i][j] != 0:
                        move(i, j, d, visited)
        else:
            visited = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if grid[i][j] != 0:
                        move(i, j, d, visited)
        dfs(depth + 1)
        grid = deepcopy(temp)

n, grid = init()
max_score = 0
dfs(0)
print(max_score)