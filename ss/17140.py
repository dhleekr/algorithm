def init():
    r, c, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(3)]

    return r, c, k, grid

def sorting(arr):
    for i in reversed(range(len(arr))):
        if arr[i] == 0:
            arr.pop(i)
    temp = []
    for i in range(1, 100):
        cnt = arr.count(i)
        if cnt:
            temp.append([i, cnt])

    temp.sort(key=lambda x : [x[1], x[0]])

    new = []
    for x in temp:
        new.append(x[0])
        new.append(x[1])

    return new

def check():
    if len(grid) < r or len(grid[0]) < c:
        return False
    if grid[r-1][c-1] == k:
        return True
    return False

def padding(length, arr):
    arr.extend([0]*(length - len(arr)))

    return arr

r, c, k, grid = init()
t = 0
while not check():
    if t >= 100:
        break
    row = len(grid)
    col = len(grid[0])
    temp = []
    if row >= col:
        max_row = 0
        for i in range(row):
            new_row = sorting(grid[i])
            temp.append(new_row)
            if max_row < len(new_row):
                if len(new_row) <= 100:
                    max_row = len(new_row)
                else:
                    max_row = 100
                    new_row = new_row[:100]

        grid = [[0]*max_row for _ in range(row)]
        for idx, new_row in enumerate(temp):
            if len(new_row) < max_row:
                new_row = padding(max_row, new_row)
            grid[idx] = new_row

    else:
        max_col = 0
        for i in range(col):
            new_col = []
            for j in range(row):
                new_col.append(grid[j][i])

            new_col = sorting(new_col)
            temp.append(new_col)
            if max_col < len(new_col):
                if len(new_col) <= 100:
                    max_col = len(new_col)
                else:
                    max_col = 100
                    new_col = new_col[:100]

        grid = [[0]*col for _ in range(max_col)]
        for idx, new_col in enumerate(temp):
            if len(new_col) < max_col:
                new_col = padding(max_col, new_col)
            for i, value in enumerate(new_col):
                grid[i][idx] = value

    t += 1

if t == 100:
    print(-1)
else:
    print(t)