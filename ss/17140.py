def init():
    r, c, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(3)]

    return r-1, c-1, k, grid

def sorting(arr):
    temp = []
    max_num = max(arr)
    for i in range(1, max_num+1):
        cnt = arr.count(i)
        if cnt != 0:
            temp.append([i, cnt])
    temp.sort(key=lambda x: [x[1], x[0]])

    new_arr = []
    for j in temp:
        new_arr.extend(j)

    return new_arr

def padding(grid):
    max_len = 0
    for temp in grid:
        if len(temp) > 100:
            temp = temp[:100]
            max_len = 100
        else:
            max_len = max(max_len, len(temp))

    for temp in grid:
        temp.extend([0]*(max_len-len(temp)))

    return grid

def transpose(grid):
    row = len(grid)
    col = len(grid[0])

    new_grid = [[0 for row in range(row)] for col in range(col)]

    for i in range(row):
        for j in range(col):
            new_grid[j][i] = grid[i][j]

    return new_grid

def calculation(grid):
    row_num = len(grid)
    col_num = len(grid[0])

    if row_num >= col_num:
        temp_grid = []
        for i in grid:
            new_arr = sorting(i)
            temp_grid.append(new_arr)
        grid = padding(temp_grid)

    else:
        temp_grid = []
        for j in range(col_num):
            temp_arr = []
            for i in range(row_num):
                temp_arr.append(grid[i][j])
            new_arr = sorting(temp_arr)
            temp_grid.append(new_arr)
        grid = padding(temp_grid)
        grid = transpose(grid)
    
    return grid


r, c, k, grid = init()

for i in range(102):
    try: 
        if grid[r][c] == k:
            print(i)
            break
        grid = calculation(grid)
    
    except:
        grid = calculation(grid)

if i == 101:
    print(-1)