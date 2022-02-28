di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, q = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(2**n)]
    L = list(map(int, input().split()))
    return n, q, grid, L

def rotate(l):
    for i in range(0, 2**n, 2**l):
        for j in range(0, 2**n, 2**l):
            temp = [row[j:j+2**l] for row in grid[i:i+2**l]]
            new = list(list(row for row in zip(*temp[::-1])))
            for ti in range(2**l):
                for tj in range(2**l):
                    grid[i + ti][j + tj] = new[ti][tj] 

def reduce():
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
                if cnt <= 2:
                    new[i][j] -= 1
    return new

def bfs(i, j):
    q = [[i, j]]
    cnt = 1
    while q:
        i, j = q.pop(0)
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < 2**n and 0 <= new_j < 2**n and grid[new_i][new_j] > 0 and visited[new_i][new_j] == 0:
                visited[new_i][new_j] = 1
                q.append([new_i, new_j])
                cnt += 1
    return cnt

n, q, grid, L = init()
for l in L:
    if l > 0:
        rotate(l)
    grid = reduce()

visited = [[0] * 2**n for _ in range(2**n)]
ans = 0
for i in range(2**n):
    for j in range(2**n):
        if visited[i][j] == 0 and grid[i][j] != 0:
            visited[i][j] = 1
            ans = max(ans, bfs(i, j))

print(sum(sum(row) for row in grid))
print(ans)