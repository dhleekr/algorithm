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

def monitor_check(grid, d, i, j):
    while True:
        i += di[d]
        j += dj[d]
        if 0 > i or i >= N or 0 > j or j >= M:
            break
        elif grid[i][j] == 6:
            break
        elif 0 <= i < N and 0 <= j < M and grid[i][j] == 0:
            grid[i][j] = '#'
    return grid
            
def monitor(grid, cctv, d, i, j):
    if cctv == 1:
        grid = monitor_check(grid, d, i, j)
    elif cctv == 2:
        grid = monitor_check(grid, d, i, j)
        d = (d+2) % 4
        grid = monitor_check(grid, d, i, j)
    elif cctv == 3:
        grid = monitor_check(grid, d, i, j)
        d = (d+1) % 4
        grid = monitor_check(grid, d, i, j)
    elif cctv == 4:
        grid = monitor_check(grid, d, i, j)
        d = (d+1) % 4
        grid = monitor_check(grid, d, i, j)
        d = (d+2) % 4
        grid = monitor_check(grid, d, i, j)
    elif cctv == 5:
        grid = monitor_check(grid, d, i, j)
        d = (d+1) % 4
        grid = monitor_check(grid, d, i, j)
        d = (d+1) % 4
        grid = monitor_check(grid, d, i, j)
        d = (d+1) % 4
        grid = monitor_check(grid, d, i, j)

    return grid

def deepcopy(grid):
    new_grid = []
    for i in range(N):
        new_grid.append(grid[i][:])
    return new_grid

def dfs(grid, idx):
    global ans
    i, j = idx.pop()
    cctv = grid[i][j]
    
    for d in range(4):
        original = deepcopy(grid)
        checked_grid = monitor(original, cctv, d, i, j)

        area = len(find_idx(checked_grid, 0))
        ans = min(ans, area)

        if idx:
            dfs(deepcopy(checked_grid), idx)
        if d == 3:
            idx.append([i, j])
            continue
            

N, M, grid = init()

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

idx = []
for i in range(1, 6):
    idx.extend(find_idx(grid, i))

if idx:
    ans = N*M
    dfs(grid, idx)
    print(ans)
else:
    print(len(find_idx(grid, 0)))