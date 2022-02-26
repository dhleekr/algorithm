def init():
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(n)]
    return n, info

def green_gravity(t, x, y):
    if t == 1:
        for i in range(2, 6):
            if green[i][y] != 0:
                green[i - 1][y] = 1
                break
        else:
            green[i][y] = 1
    elif t == 2:
        for i in range(2, 6):
            if green[i][y] != 0 or green[i][y + 1] != 0:
                green[i - 1][y] = 1
                green[i - 1][y + 1] = 1
                break
        else:
            green[i][y] = 1
            green[i][y + 1] = 1
    elif t == 3:
        for i in range(2, 6):
            if green[i][y] != 0:
                green[i - 1][y] = 1
                green[i - 2][y] = 1
                break
        else:
            green[i][y] = 1
            green[i - 1][y] = 1

def blue_gravity(t, x, y):
    if t == 1:
        for i in range(2, 6):
            if blue[i][x] != 0:
                blue[i - 1][x] = 1
                break
        else:
            blue[i][x] = 1
    elif t == 2:
        for i in range(2, 6):
            if blue[i][x] != 0:
                blue[i - 1][x] = 1
                blue[i - 2][x] = 1
                break
        else:
            blue[i][x] = 1
            blue[i - 1][x] =1
    elif t == 3:
        for i in range(2, 6):
            if blue[i][x] != 0 or blue[i][x + 1] != 0:
                blue[i - 1][x] = 1
                blue[i - 1][x + 1] = 1
                break
        else:
            blue[i][x] = 1
            blue[i][x + 1] = 1

def bingo():
    global score
    cnt = 0
    for i in range(6):
        if green[i] == [1, 1, 1, 1]:
            cnt += 1
            for idx in reversed(range(i)):
                green[idx + 1] = green[idx]
                green[idx] = [0, 0, 0, 0]
    
    for i in range(6):
        if blue[i] == [1, 1, 1, 1]:
            cnt += 1
            for idx in reversed(range(i)):
                blue[idx + 1] = blue[idx]
                blue[idx] = [0, 0, 0, 0]

    score += cnt

def light_color():
    for i in range(2):
        if sum(green[i]) != 0:
            green[1:] = green[:5]
            green[0] = [0, 0, 0, 0]
        if sum(blue[i]) != 0:
            blue[1:] = blue[:5]
            blue[0] = [0, 0, 0, 0]

n, info = init()
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]
score = 0

for block in info:
    t, x, y = block
    green_gravity(t, x, y)
    blue_gravity(t, x, y)
    bingo()
    light_color()

block_cnt = 0
for i in range(6):
    block_cnt += sum(green[i])
    block_cnt += sum(blue[i])

print(score)
print(block_cnt)