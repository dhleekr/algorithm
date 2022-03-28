di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, m, t = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    info = [list(map(int, input().split())) for _ in range(t)]
    return n, m, t, grid, info

def deepcopy(grid):
    return [row[:] for row in grid]

def rotate(x, d, k):
    for i in range(n):
        if (i + 1) % x == 0:
            if d == 0:  # CW
                for _ in range(k):
                    grid[i] = [grid[i][-1]] + grid[i][:-1]
            else:       # CCW
                for _ in range(k):
                    grid[i] = grid[i][1:] + [grid[i][0]]

def check():
    visited = [[0] * m for _ in range(n)]
    new = deepcopy(grid)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                for d in range(4):
                    visited[i][j] = 1
                    new_i = i + di[d]
                    new_j = (j + dj[d]) % m
                    if 0 <= new_i < n and grid[new_i][new_j] == grid[i][j] and visited[new_i][new_j] == 0:
                        cnt += 1
                        new[i][j] = 0
                        new[new_i][new_j] = 0
    if cnt == 0:
        denominator = sum(len([x for x in row if x != 0]) for row in grid)
        if denominator:
            avg = sum(sum(row) for row in grid) / sum(len([x for x in row if x != 0]) for row in grid)
            for i in range(n):
                for j in range(m):
                    if grid[i][j]:
                        if grid[i][j] > avg:
                            new[i][j] -= 1
                        elif grid[i][j] < avg:
                            new[i][j] += 1
    return new


n, m, t, grid, info = init()

for x, d, k in info:
    rotate(x, d, k)
    grid = check()
print(sum(sum(row) for row in grid))