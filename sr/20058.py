di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, q = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(2**n)]
    L = list(map(int, input().split()))
    return n, q, grid, L

def change_grid(l):
    if l == 0:
        return grid

    new = [[0] * 2**n for _ in range(2**n)]
    for i in range(0, 2**n, 2**l):
        for j in range(0, 2**n, 2**l):
            sub_grid = [row[j : j + 2**l] for row in grid[i : i + 2**l]] # 부분 격자
            temp_grid = [list(a) for a in zip(*sub_grid[::-1])] # 시계 방향 90도
            for ni in range(2**l):
                for nj in range(2**l):
                    new[i + ni][j + nj] = temp_grid[ni][nj]
    return new

def reduce_ice():
    new = [row[:] for row in grid]
    for i in range(2**n):
        for j in range(2**n):
            if grid[i][j] > 0:
                cnt = 0
                for d in range(4):
                    new_i = i + di[d]
                    new_j = j + dj[d]
                    if 0 <= new_i < 2**n and 0 <= new_j < 2**n and grid[new_i][new_j] > 0:
                        cnt += 1
                if cnt < 3:
                    new[i][j] -= 1
    return new

def bfs():
    visited = [[0] * 2**n for _ in range(2**n)]
    max_cnt = 0
    for i in range(2**n):
        for j in range(2**n):
            if visited[i][j] == 0 and grid[i][j] > 0:
                visited[i][j] = 1
                cnt = 1
                q = [[i, j]]
                while q:
                    i, j = q.pop(0)
                    for d in range(4):
                        new_i = i + di[d]
                        new_j = j + dj[d]
                        if 0 <= new_i < 2**n and 0 <= new_j < 2**n and grid[new_i][new_j] > 0 and visited[new_i][new_j] == 0:
                            visited[new_i][new_j] = 1
                            q.append([new_i, new_j])
                            cnt += 1
                max_cnt = max(max_cnt, cnt)
    return max_cnt


n, q, grid, L = init()
grid = change_grid(0)

for l in L:
    grid = change_grid(l)
    grid = reduce_ice()

print(sum(sum(row) for row in grid))
print(bfs())