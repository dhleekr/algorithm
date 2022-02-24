di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n = int(input())
    k = int(input())
    apple = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
    l = int(input())
    info = []
    for _ in range(l):
        x, c = input().split()
        info.append([int(x), c])
    return n, k, apple, l, info

n, k, apple, l, info = init()
grid = [[0] * n for _ in range(n)]
grid[0][0] = -1
for i, j in apple:
    grid[i][j] = 1
t = 0
d = 0
i = 0
j = 0
snake = [[i, j]]
while True:
    t += 1
    new_i = i + di[d]
    new_j = j + dj[d]
    if not (0 <= new_i < n and 0 <= new_j < n) or [new_i, new_j] in snake:
        break
    else:
        snake.append([new_i, new_j])
        if grid[new_i][new_j] == 1:
            grid[new_i][new_j] = -1
        else:
            grid[new_i][new_j] = -1
            si, sj = snake.pop(0)
            grid[si][sj] = 0

    if info and t == info[0][0]:
        _, c = info.pop(0)
        if c == 'D':
            d = (d + 1) % 4
        elif c == 'L':
            d = (d - 1) % 4
    i = new_i
    j = new_j

print(t) 