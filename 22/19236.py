di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

def init():
    grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        temp = list(map(int, input().split()))
        for j in range(4):
            a, b = temp[2*j : 2*j + 2]
            b -= 1
            grid[i][j] = [a, b]
    return grid

def fish_rotation(idx, d, shark):
    i, j = idx
    for _ in range(8):
        new_i = i + di[d]
        new_j = j + dj[d]
        if 0 <= new_i < 4 and 0 <= new_j < 4 and (new_i, new_j) != shark:
            return d, True
        else:
            d = (d + 1) % 8
    return d, False

def find_index(a, grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j][0] == a:
                return (i, j)
    return None

def fish_move(grid, shark):
    for a in range(1, 17):
        idx = find_index(a, grid)
        if idx == None:
            pass
        else:
            i, j = idx
            d = grid[i][j][1]
            d, info = fish_rotation(idx, d, shark)
            if info:
                grid[i][j][1] = d
                new_i = i + di[d]
                new_j = j + dj[d]
                grid[i][j], grid[new_i][new_j] = grid[new_i][new_j], grid[i][j]
    return grid

def deepcopy(grid):
    new_grid = []
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(grid[i][j][:])
        new_grid.append(temp)
    return new_grid

def dfs(i, j, score, grid):
    global answer

    score += grid[i][j][0]
    d = grid[i][j][1]
    grid[i][j][0] = 0
    shark = (i, j)
    
    grid = fish_move(grid, shark)

    answer = max(answer, score)

    for step in range(1, 4):
        new_i = i + step * di[d]
        new_j = j + step * dj[d]

        if 0 <= new_i < 4 and 0 <= new_j < 4 and grid[new_i][new_j][0] > 0:
            dfs(new_i, new_j, score, [[b[:] for b in a] for a in grid])

grid = init()
answer = 0
dfs(0, 0, 0, grid)
print(answer)