def init():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    ds_list = [list(map(int, input().split())) for _ in range(M)]

    return N, M, grid, ds_list

def throw_ice(grid, ds):
    d = ds[0] - 1
    sx = N // 2
    sy = N // 2

    for s in range(1, ds[1]+1):
        new_i = sx + s*di[d]
        new_j = sy + s*dj[d]
        if 0 <= new_i < N and 0 <= new_j < N:
            grid[new_i][new_j] = 0

def marble_move():
    flatten_grid = [[0]]*(N**2 - 1)
    idx = 0
    for (i, j) in order_list:
        flatten_grid[idx] = grid[i][j]
        idx += 1
    zero_cnt = flatten_grid.count(0)
    for _ in range(zero_cnt):
        flatten_grid.remove(0)
    return flatten_grid

def order():
    order_idx = [[0]]*(N**2-1)
    sx = N // 2
    sy = N // 2
    direction = [2, 1, 3, 0]
    distance = 0
    cnt = 0
    d = 0
    idx = 0
    
    while idx < N**2 - 1:
        if cnt % 2 == 0:
            distance += 1
        for _ in range(distance):
            if idx >= N**2-1:
                break
            sx = sx + di[direction[d]]
            sy = sy + dj[direction[d]]
            order_idx[idx] = [sx, sy]
            idx += 1

        d = (d+1) % 4
        cnt += 1

    return order_idx

def boom(flatten_grid, res):
    i = len(flatten_grid) - 1
    boom_cnt = 0
    while i > 0 :
        a = flatten_grid[i]
        cnt = 1
        while i - cnt >= 0 and flatten_grid[i-cnt] == a:
            cnt += 1
        
        if cnt >= 4:
            for j in range(cnt):
                res += flatten_grid[i-j]
                boom_cnt += 1
                del flatten_grid[i-j]
        i -= cnt
    
    return boom_cnt, res

def change(flatten_grid):
    new_flatten = []
    i = 0
    while i < len(flatten_grid):
        a = flatten_grid[i]
        cnt = 1
        while i + cnt < len(flatten_grid) and flatten_grid[i+cnt] == a:
            cnt += 1
        
        new_flatten.extend([cnt, a])

        i += cnt

    return new_flatten[:N**2-1]



di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M, grid, ds_list = init()
order_list = order()
res = 0

for ds in ds_list:
    throw_ice(grid, ds)
    flatten = marble_move()
    while True:
        boom_cnt, res = boom(flatten, res)
        if boom_cnt == 0:
            break
    flatten = change(flatten)
    grid = [[0]*N for _ in range(N)]
    for idx, value in enumerate(flatten):
        i, j = order_list[idx]
        grid[i][j] = value

print(res)