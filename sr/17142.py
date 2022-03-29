di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, grid

def combination(array, r):
    if r == 0:
        return []
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for n in combination(array[i+1:], r-1):
                yield [array[i]] + n

def bfs(starts):
    q = []
    for i, j in starts:
        q.append((i, j, 0))
    
    temp = [row[:] for row in grid]
    visited = [[0]*n for _ in range(n)]
    while q:
        i, j, t = q.pop(0)
        if visited[i][j]:
            continue
        visited[i][j] = t
        temp[i][j] = 2
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] != 1:
                q.append((new_i, new_j, t+1))

    result = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                if visited[i][j] == 0:
                    return 1e10
                result = max(result, visited[i][j])
    return result


n, m, grid = init()
virus = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            virus.append((i, j))

answer = 1e10
for starts in combination(virus, m):
    answer = min(answer, bfs(starts))
if answer == 1e10:
    print(-1)
else:
    print(answer)