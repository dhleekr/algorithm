dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def init():
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(n)]
    return n, info

def draw(x, y, d, g):
    dragon_curve = [[x, y], [x + dx[d], y + dy[d]]]
    for _ in range(g):
        pivot = dragon_curve[-1]
        temp = []
        for j in range(len(dragon_curve) - 2, -1, -1):
            x, y = dragon_curve[j]
            new_x = pivot[0] + pivot[1] - y
            new_y = -pivot[0] + pivot[1] + x
            temp.append([new_x, new_y])
        dragon_curve.extend(temp)
    return dragon_curve

def check(i, j):
    if grid[i][j] == 0 or grid[i + 1][j] == 0 or grid[i][j + 1] == 0 or grid[i + 1][j + 1] == 0:
        return False
    else:
        return True

def check_square():
    cnt = 0
    for i in range(100):
        for j in range(100):
            if check(i, j):
                cnt += 1

    return cnt

n, info = init()
grid = [[0] * 101 for _ in range(101)]
for x, y, d, g in info:
    dragon_curve = draw(x, y, d, g)
    for x, y in dragon_curve:
        if grid[y][x] == 0:
            grid[y][x] = 1

print(check_square())