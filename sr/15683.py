di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, grid

def deepcopy(grid):
    new = []
    for i in range(n):
        new.append(grid[i][:])
    return new

def find_cctv():
    cctv = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0 and grid[i][j] != 6:
                cctv.append([i, j])
    return cctv

def count_zeros():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                cnt += 1
    return cnt

def watch(i, j, d):
    while True:
        i += di[d]
        j += dj[d]
        if not (0 <= i < n and 0 <= j < m):
            break
        if grid[i][j] == 6:
            break
        elif grid[i][j] == 0:
            grid[i][j] = -1

def case(num):
    if num == 1:
        return [[0], [1], [2], [3]]
    elif num == 2:
        return [[0, 2], [1, 3]]
    elif num == 3:
        return [[0, 1], [1, 2], [2, 3], [3, 0]]
    elif num == 4:
        return [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
    elif num == 5:
        return [[0, 1, 2, 3]]

def dfs(cctv):
    global min_area, grid
    if not cctv:
        min_area = min(min_area, count_zeros())
        return

    i, j = cctv.pop()
    num = grid[i][j]
    temp = deepcopy(grid)

    for d_list in case(num):
        for d in d_list:
            watch(i, j, d)
        dfs(cctv)
        grid = deepcopy(temp)
    cctv.append([i, j])


n, m, grid = init()
cctv = find_cctv()
min_area = 1e10
dfs(cctv)
print(min_area)