def init():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    return N, M, grid

def find_idx(grid, a):
    idx = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == a:
                idx.append([i, j])

    return idx

def virus_spread(grid, virus_idx):
    while virus_idx:
        i, j = virus_idx.pop(0)
        visited[i][j] = 1
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]

            if 0 <= new_i < N and 0 <= new_j < M and not visited[new_i][new_j] and grid[new_i][new_j] == 0:
                virus_idx.append([new_i, new_j])
                visited[new_i][new_j] = 1
                grid[new_i][new_j] = 2
    
    return grid

def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for n in combination(array[i+1:], r-1):
                yield [array[i]] + n

def make_wall(idx):
    for i,j in idx:
        grid[i][j] = 1

def deepcopy(grid):
    new_grid = []
    for i in range(N):
        new_grid.append(grid[i][:])

    return new_grid

N, M, first_grid = init()

empty_idx = find_idx(first_grid, 0)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

max_area = 0
for idx in combination(empty_idx, 3):
    virus_idx = find_idx(first_grid, 2)
    grid = deepcopy(first_grid)
    visited = [[0]*M for _ in range(N)]
    make_wall(idx)
    grid = virus_spread(grid, virus_idx)
    area = len(find_idx(grid, 0))

    if max_area < area:
        max_area = area

print(max_area)