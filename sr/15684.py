def init():
    n, m, h = map(int, input().split())
    grid = [[-1] * n for _ in range(h)]
    for _ in range(m):
        a, b = map(lambda x : int(x) - 1, input().split())
        grid[a][b] = b + 1
        grid[a][b + 1] = b
    return n, m, h, grid

def check():
    for j in range(n):
        original = j
        for i in range(h):
            if grid[i][j] != -1:
                j = grid[i][j]
        
        if original != j:
            return False
    return True

def combination(arr, r):
    for i in range(len(arr)):
        if r == 0:
            yield []
        elif r == 1:
            yield [arr[i]]
        else:
            for j in combination(arr[i+1:], r - 1):
                yield [arr[i]] + j

def find_idx():
    res = []
    for i in range(h):
        for j in range(n):
            if grid[i][j] == -1 and j != n - 1:
                res.append([i, j])
    return res

def deepcopy(grid):
    return [row[:] for row in grid]

n, m, h, grid = init()
empty = find_idx()

cnt = 0
if not check():
    done = False
    while cnt < 3:
        cnt += 1
        for _list in combination(empty, cnt):
            temp_grid = deepcopy(grid)
            for a, b in _list:
                grid[a][b] = b + 1
                grid[a][b + 1] = b
            if check():
                done = True
                break
            grid = temp_grid
        if done:
            break
else:
    done = True

if not done:
    print(-1)
else:
    print(cnt)