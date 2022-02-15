di = [0, 0, 0, -1, 1] # 처음꺼는 아무 의미 x, 주어지는 숫자 1, 2, 3,4  라서
dj = [0, 1, -1, 0, 0]

def init():
    n, m, i, j, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    directions = list(map(int, input().split()))
    return n, m, i, j, k, grid, directions

def rolling(d):
    if d == 1:
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif d == 2:
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif d == 3:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    else:
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]

def move(i, j, d):
    if 0 <= i + di[d] < n and 0 <= j + dj[d] < m:
        i += di[d]
        j += dj[d]
        rolling(d)
        if grid[i][j] == 0:
            grid[i][j] = dice[5]
        else:
            dice[5] = grid[i][j]
            grid[i][j] = 0
        print(dice[0])
    return i, j


n, m, i, j, k, grid, directions = init()
dice = [0] * 6

for d in directions:
    i, j = move(i, j, d)