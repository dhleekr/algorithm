from copy import deepcopy

def init():
    fish_information = [list(map(int, input().split())) for _ in range(4)]
    grid = []
    for i in range(4):
        j = 0 
        row = []
        while j < 8:
            if j % 2 == 0:
                temp = []
            temp.append(fish_information[i][j])

            if len(temp) == 2:
                temp[1] -= 1
                row.append(temp)
            j += 1

        grid.append(row)

    return grid

def fish_rotation(idx, d, grid, shark):
    i, j = idx
    while True:
        new_i = i + di[d]
        new_j = j + dj[d]

        if 0 <= new_i < 4 and 0 <= new_j < 4 and (new_i, new_j) != shark:
            return d
        else:
            d = (d+1) % 8

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
            d = fish_rotation(idx, d, grid, shark)
            grid[i][j][1] = d
            new_i = i + di[d]
            new_j = j + dj[d]

            grid[i][j], grid[new_i][new_j] = grid[new_i][new_j], grid[i][j]

    return grid

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
            dfs(new_i, new_j, score, deepcopy(grid))

    

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]
grid = init()

answer = 0
dfs(0, 0, 0, grid)
print(answer)