def init():
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(n)]
    return n, info

def stack(grid, type, j):
    i = 0
    if type == 1:
        while True:
            if i == 5:
                grid[i][j] = 1
                break
            if grid[i + 1][j] == 0:
                i += 1
            else:
                grid[i][j] = 1
                break
    elif type == 2:
        while True:
            if i == 5:
                grid[i][j] = 1
                grid[i][j + 1] = 1
                break
            if grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                i += 1
            else:
                grid[i][j] = 1
                grid[i][j + 1] = 1
                break
    elif type == 3:
        while True:
            if i == 4:
                grid[i][j] = 1
                grid[i + 1][j] = 1
                break
            if grid[i + 1][j] == 0 and grid[i + 2][j] == 0:
                i += 1
            else:
                grid[i][j] = 1
                grid[i + 1][j] = 1
                break
    return grid

def boom(grid):
    global cnt
    for i in range(5, -1, -1):
        while sum(grid[i]) == 4:
            cnt += 1
            grid[1:i+1] = grid[:i]
            grid[0] = [0, 0, 0, 0]

def reduce_top(grid):
    new = [[0] * 4 for _ in range(6)]
    top = 0
    for i in range(2):
        if grid[i] != [0, 0, 0, 0]:
            top += 1
    if top == 2:
        new[2:] = grid[:-top]
        return new
    elif top == 1:
        new[2:] = grid[1:-top]
        return new
    else:
        return grid
    

n, info = init()
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]
cnt = 0
for type, i, j in info:
    green = stack(green, type, j)
    if type == 2:
        blue = stack(blue, 3, i)
    elif type == 3:
        blue = stack(blue, 2, i)
    else:
        blue = stack(blue, 1, i)
    
    boom(green)
    boom(blue)

    green = reduce_top(green)
    blue = reduce_top(blue)

g = sum(sum(row) for row in green)
b = sum(sum(row) for row in blue)

print(cnt)
print(g + b)