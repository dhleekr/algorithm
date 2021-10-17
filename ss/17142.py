from collections import deque
def init():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    return N, M, grid

def deepcopy(grid):
    new_grid = []
    for i in range(N):
        new_grid.append(grid[i][:])
    return new_grid

def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for n in combination(array[i+1:], r-1):
                yield [array[i]] + n

def bfs(starts):
    q = deque()
    for i, j in starts:
        q.append((i, j, 0))
    
    temp = deepcopy(grid)
    visited = [[0]*N for _ in range(N)]
    result = 0
    while q:
        i, j, t = q.popleft()
        if visited[i][j]:
            continue
        visited[i][j] = t
        temp[i][j] = 2
        for di, dj in move:
            new_i = i + di
            new_j = j + dj
            if 0 <= new_i < N and 0 <= new_j < N and grid[new_i][new_j] != 1:
                q.append((new_i, new_j, t+1))
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                if visited[i][j] == 0:
                    return float("inf")
                result = max(result, visited[i][j])
                
    return result


N, M, grid = init()

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

virus = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            virus.append((i, j))

answer = float("inf")

for start in combination(virus, M):
    answer = min(answer, bfs(start))

if answer == float('inf'):
    print(-1)
else:
    print(answer)