def init():
    R, C, T = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]

    return R, C, T, grid

def deepcopy(grid):
    new = []
    for i in range(R):
        temp = grid[i][:]
        new.append(temp)
    return new

def find_idx():
    indices = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                indices.append([i, j])
    return indices

def spread(grid):
    indices = find_idx()
    copy = deepcopy(grid)

    for idx in indices:
        i, j = idx

        amount = 0
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < R and 0 <= new_j < C and copy[new_i][new_j] != -1:
                grid[new_i][new_j] += copy[i][j] // 5
                amount += copy[i][j] // 5
        
        grid[i][j] -= amount

    return grid

def air_clean():
    air = []
    for i in range(R):
        if grid[i][0] == -1:
            air.append(i)
            break

    copy = deepcopy(grid)
    
    for j in range(1, C-1):
        new_j = j + dj[3]
        grid[i][new_j] = copy[i][j]
        grid[i+1][new_j] = copy[i+1][j]

    for j in range(i, 0, -1):
        new_j = j + di[0]
        grid[new_j][C-1] = copy[j][C-1]
        
    for j in range(C-1, 0, -1):
        new_j = j + dj[2]
        grid[0][new_j] = copy[0][j]
        grid[R-1][new_j] = copy[R-1][j]
    
    for j in range(0, i):
        new_j = j + di[1]
        grid[new_j][0] = copy[j][0]

    for j in range(i+1, R-1):
        new_j = j + di[1]
        grid[new_j][C-1] = copy[j][C-1]

    for j in range(R-1, i, -1):
        new_j = j + di[0]
        grid[new_j][0] = copy[j][0]
    
    grid[i][0] = -1
    grid[i+1][0] = -1
    grid[i][1] = 0
    grid[i+1][1] = 0

R, C, T, grid = init()

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for _ in range(T):
    grid = spread(grid)
    air_clean()
print(sum(sum(row) for row in grid)+2)