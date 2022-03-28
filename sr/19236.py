di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

def init():
    grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        temp = list(map(int, input().split()))
        for j in range(0, 8, 2):
            grid[i][j // 2] = [temp[j], temp[j + 1] - 1]
    return grid

def find_idx(grid, num):
    for i in range(4):
        for j in range(4):
            if grid[i][j][0] == num:
                return [i, j]
    return None

def fish_move(grid, shark):
    for num in range(1, 17):
        idx = find_idx(grid, num)
        if idx == None:
            continue
        else:
            i, j = idx
            d = grid[i][j][1]
            for _ in range(8):
                new_i = i + di[d]
                new_j = j + dj[d]
                if 0 <= new_i < 4 and 0 <= new_j < 4 and [new_i, new_j] != shark:
                    grid[i][j][1] = d
                    grid[i][j], grid[new_i][new_j] = grid[new_i][new_j], grid[i][j]
                    break
                d = (d + 1) % 8
    return grid

def deepcopy(grid):
    return [[e[:] for e in row] for row in grid]

def shark_move(i, j, total, grid):
    global eat
    
    total += grid[i][j][0]
    d = grid[i][j][1]
    grid[i][j][0] = 0
    shark = [i, j]

    grid = fish_move(grid, shark)
    eat = max(eat, total)

    for s in range(1, 4):
        new_i = i + s * di[d]
        new_j = j + s * dj[d]
        if 0 <= new_i < 4 and 0 <= new_j < 4 and grid[new_i][new_j][0] != 0:
            shark_move(new_i, new_j, total, deepcopy(grid))

grid = init()
eat = 0
shark_move(0, 0, 0, grid)
print(eat)