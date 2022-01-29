di = [0, 1, 0, -1] # 동 남 서 북
dj = [1, 0, -1, 0]

def init():
    n = int(input())
    grid = [[0]*n for _ in range(n)]

    k = int(input())

    for _ in range(k):
        i, j = map(int, input().split())
        grid[i-1][j-1] = 1

    l = int(input())
    directions = dict()
    for _ in range(l):
        x, c = input().split()
        directions[int(x)] = c

    return n, grid, directions

def move(i, j, d, snake, grid):
    n = len(grid)
    new_i = i + di[d]
    new_j = j + dj[d]
    info = True

    if 0 <= new_i < n and 0 <= new_j < n and [new_i, new_j] not in snake:
        snake.append([new_i, new_j])
        if grid[new_i][new_j] == 1:
            grid[new_i][new_j] = 0
        else:
            snake.pop(0)
    else: # 끝
        info = False
    
    return new_i, new_j, snake, grid, info

def turn(d, direction):
    if direction == 'L':
        d = (d-1)%4 
    elif direction == 'D':
        d = (d+1)%4
    return d

n, grid, directions = init()

snake = [[0, 0]]
t = 0
i = 0
j = 0
d = 0
while True:
    i, j, snake, grid, info = move(i, j, d, snake, grid)
    t += 1
    if not info:
        break

    if t in directions.keys():
        d = turn(d, directions[t])


print(t)