di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, grid

def move(i, j, d, visited):
    while True:
        new_i = i + di[d]
        new_j = j + dj[d]
        if not(0 <= new_i < n and 0 <= new_j < n):
            break
        if grid[new_i][new_j]:
            if grid[i][j] == grid[new_i][new_j] and visited[new_i][new_j] == 0:
                grid[new_i][new_j] *= 2
                grid[i][j] = 0
                visited[new_i][new_j] = 1
            break
        else:
            grid[new_i][new_j] = grid[i][j]
            grid[i][j] = 0

        i = new_i
        j = new_j

def tilt(d):
    visited = [[0] * n for _ in range(n)]
    if d == 0:
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    move(i, j, d, visited)
    elif d == 1:
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if grid[i][j]:
                    move(i, j, d, visited)
    elif d == 2:
        for i in range(n):
            for j in range(1, n):
                if grid[i][j]:
                    move(i, j, d, visited)
    elif d == 3:
        for i in range(1, n):
            for j in range(n):
                if grid[i][j]:
                    move(i, j, d, visited)
    
def dfs(depth):
    global grid, ans
    if depth == 5:
        ans = max(ans, max(max(row) for row in grid))
        return

    temp_grid = [row[:] for row in grid]
    for d in range(4):
        tilt(d)
        dfs(depth + 1)
        grid = [row[:] for row in temp_grid]
        
n, grid = init()
ans = 0
dfs(0)
print(ans)