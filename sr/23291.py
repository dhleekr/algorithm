def init():
    n, k = map(int, input().split())
    fishbowl = list(map(int, input().split()))
    return n, k, fishbowl

def deepcopy(grid):
    new = []
    for i in range(len(grid)):
        new.append(grid[i][:])
    return new

def min_plus():
    min_val = min(fishbowl)
    for i in range(n):
        if fishbowl[i] == min_val:
            fishbowl[i] += 1

def build1(fishbowl):
    grid = [[0] * n for _ in range(n)]
    grid[-1] = fishbowl
    w, h = 1, 1
    idx = 0
    while idx + h < n:
        next_idx = idx + h
        for temp_i, j in enumerate(range(idx, idx - w, -1)):
            for temp_j, i in enumerate(range(n - h, n)):
                grid[n - 2 - temp_i][next_idx - temp_j] = grid[i][j]
                grid[i][j] = 0

        idx = next_idx
        if w == h:
            h += 1
        else:
            w += 1

    return grid

def fishnum_control(grid):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    visited = [[0] * n for _ in range(n)]
    new = deepcopy(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                visited[i][j] = 1
                for d in range(4):
                    new_i = i + di[d]
                    new_j = j + dj[d]
                    if 0 <= new_i < n and 0 <= new_j < n and visited[new_i][new_j] == 0 and grid[new_i][new_j]:
                        temp = abs(grid[i][j] - grid[new_i][new_j]) // 5
                        if temp > 0:
                            if grid[i][j] > grid[new_i][new_j]:
                                new[i][j] -= temp
                                new[new_i][new_j] += temp
                            elif grid[i][j] < grid[new_i][new_j]:
                                new[i][j] += temp
                                new[new_i][new_j] -= temp
    return new

def flatten(grid):
    line = [] 
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                line.append(grid[i][j])
            else:
                break
    return line

def build2(fishbowl):
    grid = [[0] * n for _ in range(n)]
    grid[-1] = fishbowl
    half = n // 2
    idx = 0
    h = 1
    for _ in range(2):
        for temp_i, i in enumerate(range(n - h, n)):
            for temp_j, j in enumerate(range(idx, idx + half)):
                grid[n - 1 - h - temp_i][n - 1 - temp_j] = grid[i][j]
                grid[i][j] = 0
        h += 1
        idx += half
        half //= 2
    return grid

def check():
    return (max(fishbowl) - min(fishbowl)) <= k


n, k, fishbowl = init()

cnt = 0
while not check():
    min_plus()
    grid = build1(fishbowl)
    grid = fishnum_control(grid)
    fishbowl = flatten(grid)
    grid = build2(fishbowl)
    grid = fishnum_control(grid)
    fishbowl = flatten(grid)
    cnt += 1

print(cnt)