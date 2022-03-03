di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def init():
    n, m, x, y, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    command = list(map(lambda x : int(x) - 1, input().split()))
    return n, m, x, y, k, grid, command

def move(i, j, d):
    new_i = i + di[d]
    new_j = j + dj[d]
    if not (0 <= new_i < n and 0 <= new_j < m):
        return None
    
    if d == 0:
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif d == 1:
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif d == 2:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif d == 3:
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]

    if grid[new_i][new_j] == 0:
        grid[new_i][new_j] = dice[5]
    else:
        dice[5] = grid[new_i][new_j]
        grid[new_i][new_j] = 0

    return [new_i, new_j]

n, m, x, y, k, grid, command = init()
dice = [0] * 6 # 위, 뒤, 오, 왼, 앞, 바
for d in command:
    idx = move(x, y, d)
    if idx:
        x, y = idx
        print(dice[0])