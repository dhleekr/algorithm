di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

def rolling(d):
    if d == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif d == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif d == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif d == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
        

n, m, i, j, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]
for d in commands:
    if 0 <= i + di[d] < n and 0 <= j + dj[d] < m:
        i += di[d]
        j += dj[d]
        rolling(d)
        if grid[i][j] == 0:
            grid[i][j] = dice[6]
        else:
            dice[6] = grid[i][j]
            grid[i][j] = 0
        print(dice[1])