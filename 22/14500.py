di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, grid

def dfs(i, j, depth, area):
    global max_area
    if max_area >= area + max_val * (3 - depth):
        return

    if depth == 3:
        max_area = max(max_area, area)
        return
    
    for d in range(4):
        new_i = i + di[d]
        new_j = j + dj[d]

        if 0 <= new_i < n and 0 <= new_j < m and not visited[new_i][new_j]:
            if depth == 1:
                visited[new_i][new_j] = 1
                dfs(i, j, depth + 1, area + grid[new_i][new_j])
                visited[new_i][new_j] = 0

            visited[new_i][new_j] = 1
            dfs(new_i, new_j, depth + 1, area + grid[new_i][new_j])
            visited[new_i][new_j] = 0


n, m, grid = init()

visited = [[0] * m for _ in range(n)]
max_area = 0
max_val = max(map(max, grid))
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, grid[i][j])
        visited[i][j] = 0

print(max_area)