di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, l, r = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, l, r, grid

def bfs():
    visited = [[0] * n for _ in range(n)]
    new_grid = [[0] * n for _ in range(n)]
    done = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                block = [[i, j]]
                total = grid[i][j]
                q = [[i, j]]
                while q:
                    qi, qj = q.pop(0)
                    for d in range(4):
                        new_i = qi + di[d]
                        new_j = qj + dj[d]
                        if 0 <= new_i < n and 0 <= new_j < n and visited[new_i][new_j] == 0 and\
                            l <= abs(grid[qi][qj] - grid[new_i][new_j]) <= r:
                            visited[new_i][new_j] = 1
                            block.append([new_i, new_j])
                            q.append([new_i, new_j])
                            total += grid[new_i][new_j]
                if len(block) > 1:
                    for bi, bj in block:
                        new_grid[bi][bj] = total // len(block)
                    done = True
                else:
                    new_grid[i][j] = grid[i][j]
    return new_grid, done


n, l, r, grid = init()
cnt = 0
while True:
    grid, done = bfs()
    if not done:
        break
    cnt += 1
print(cnt)