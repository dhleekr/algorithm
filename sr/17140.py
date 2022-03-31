def init():
    r, c, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(3)]
    return r - 1, c - 1, k, grid

def custom_sort(arr):
    res = []
    max_val = max(arr)
    for val in range(1, max_val + 1):
        cnt = arr.count(val)
        if cnt:
            res.append([val, arr.count(val)])
    res.sort(key=lambda x : (x[1], x[0]))
    return sum(res, []) # 2차원 리스트 -> 1차원 리스트

def R(grid):
    for i in range(len(grid)):
        grid[i] = custom_sort(grid[i])

    max_len = max(len(row) for row in grid)

    for i in range(len(grid)):
        for _ in range(max_len - len(grid[i])):
            grid[i].append(0)
    return grid


r, c, k, grid = init()

t = 0
while (len(grid) <= r or len(grid[0]) <= c) or grid[r][c] != k:
    t += 1
    if len(grid) >= len(grid[0]):
        grid = R(grid)
    else:
        grid = [list(x) for x in zip(*grid)]
        grid = R(grid)
        grid = [list(x) for x in zip(*grid)]

    if t > 101:
        t = -1
        break

print(t)