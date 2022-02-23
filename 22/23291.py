di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    return n, k, arr

def add_fish():
    temp = []
    min_val = 1e10
    for i in range(n):
        for j in range(n):
            print(i, j, len(grid), len(grid[0]))
            if grid[i][j] != -1:
                if grid[i][j] < min_val:
                    min_val = grid[i][j]
                    temp.append([i, j])
                elif grid[i][j] == min_val:
                    temp.append([i, j])
    for i, j in temp:
        grid[i][j] += 1

def control():
    new = [row[:] for row in grid]
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] != -1:
                for d in range(4):
                    new_i = i + di[d]
                    new_j = j + dj[d]
                    if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] != -1 and visited[new_i][new_j] == 0:
                        diff = abs(grid[new_i][new_j] - grid[i][j]) // 5
                        if diff > 0:
                            if grid[new_i][new_j] > grid[i][j]:
                                new[new_i][new_j] -= diff
                                new[i][j] += diff
                            elif grid[new_i][new_j] < grid[i][j]:
                                new[i][j] -= diff
                                new[new_i][new_j] += diff
                visited[i][j] = 1
    return new

def roll(grid):
    h = 1
    w = 1
    start = 0
    while h <= n - start - w:
        for i in range(h):
            for j in range(w):
                new_i = w - j
                new_j = start + w + i
                grid[new_i][new_j] = grid[i][j + start]
                grid[i][j + start] = -1
        start += w
        if h == w:
            h += 1
        else:
            w += 1
    
    grid = control()

    new_arr = []
    for j in range(n):
        for i in range(n):
            if grid[i][j] != -1:
                new_arr.append(grid[i][j])
    new = [[-1] * n for _ in range(n)]
    new[0] = new_arr
    return new

def fold(grid):
    print(grid)
    start = 0
    h = 1
    w = n // 2
    for _ in range(2):
        for i in range(h):
            for j in range(w):
                new_i = 2 * h - i - 1
                new_j = 2 * w + start - w - 1
                grid[new_i][new_j] = grid[i][j + start]
                grid[i][j + w] = -1
        start += w
        w //= 2
        h *= 2
    grid = control()

    new_arr = []
    for j in range(n):
        for i in range(n):
            if grid[i][j] != -1:
                new_arr.append(grid[i][j])
    new = [[-1] * n for _ in range(n)]
    new[0] = new_arr
    print(new_arr)
    return new
                
def finish():
    max_val = max(max(row) for row in grid)
    min_val = min(min(row) for row in grid)
    return (max_val - min_val) <= k


n, k, arr = init()
grid = [[-1] * n for _ in range(n)]
grid[0] = arr

cnt = 0
while not finish():
    print(grid)
    add_fish()
    grid = roll(grid)
    grid = fold(grid)
    cnt += 1

print(cnt)