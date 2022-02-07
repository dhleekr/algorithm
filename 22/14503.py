di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def init():
    n, m = map(int, input().split())
    si, sj, d = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, si, sj, d, grid


n, m, si, sj, d, grid = init()

visited = [[0] * m for _ in range(n)]
q = [[si, sj]]
while q:
    i, j = q.pop(0)
    visited[i][j] = 1

    cnt = 0
    while cnt < 4:
        d = (d - 1) % 4
        new_i = i + di[d]
        new_j = j + dj[d]
        if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] != 1 and not visited[new_i][new_j]:
            q.append([new_i, new_j])
            break
        cnt += 1
    
    if cnt == 4:
        new_i = i - di[d]
        new_j = j - dj[d]
        if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] != 1:
            q.append([new_i, new_j])
        else:
            break

print(sum(sum(row) for row in visited))