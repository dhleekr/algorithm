di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def move(grid, ball, i, j, d):
    end = False
    check = False
    grid[i][j] = '.'

    while True:
        i += di[d]
        j += dj[d]

        if grid[i][j] == "O":
            end = True
            check = True
            return grid, check, end
        
        if grid[i][j] == "#":
            check = True
            i -= di[d]
            j -= dj[d]
            grid[i][j] = ball
            return grid, check, end

n, m = map(int, input().split())
grid = [list(input() for _ in range(n))]

# grid, check, end = move(grid, "B", 1, 3, 2)
print(grid)
# print(check)