di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    info = [list(map(int, input().split())) for _ in range(m)]
    return n, m, grid, info

def magic(i, j):
    cnt = 0
    for d in range(2, 9, 2):
        new_i = i + di[d]
        new_j = j + dj[d]
        if 0 <= new_i < n and 0 <= new_j < n:
            if grid[new_i][new_j]:
                cnt += 1
    grid[i][j] += cnt

n, m, grid, info = init()
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
for d, s in info:
    visited = [[0] * n for _ in range(n)]
    for _ in range(len(cloud)):
        ci, cj = cloud.pop()
        ci = (ci + s * di[d]) % n
        cj = (cj + s * dj[d]) % n
        grid[ci][cj] += 1
        visited[ci][cj] = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                magic(i, j)
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and visited[i][j] == 0:
                grid[i][j] -= 2
                cloud.append([i, j])

print(sum(sum(row) for row in grid))