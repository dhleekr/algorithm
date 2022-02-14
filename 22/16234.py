di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, l, r = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    return n, l, r, grid

def bfs(i, j):
    completed = [[i, j]]
    q = [[i, j]]
    visited[i][j] = 1
    total = grid[i][j]
    cnt = 1

    while q:
        i, j = q.pop(0)
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]

            if 0 <= new_i < n and 0 <= new_j < n and visited[new_i][new_j] == -1:
                if l <= abs(grid[new_i][new_j]- grid[i][j]) <= r:
                    q.append([new_i, new_j])
                    visited[new_i][new_j] = 1
                    total += grid[new_i][new_j]
                    cnt += 1
                    completed.append([new_i, new_j])
        
    for i, j in completed:
        grid[i][j] = total // cnt


n, l, r, grid = init()

t = 0
while True:
    visited = [[-1]*n for _ in range(n)]
    num = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                bfs(i, j)
                num += 1
    if num == n*n:
        break
    t += 1

print(t)