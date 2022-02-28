def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    magic = []
    for _ in range(m):
        d, s = map(int, input().split())
        d -= 1
        magic.append([d, s])
    return n, m, grid, magic

def blizard(d, s):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    si, sj = n // 2, n // 2
    for step in range(1, s + 1):
        new_i = si + step * di[d]
        new_j = sj + step * dj[d]
        if 0 <= new_i < n and 0 <= new_j < n:
            grid[new_i][new_j] = 0

def get_line_idx():
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    line = []

    i, j = n // 2, n // 2
    step = 0
    d = 0
    cnt = 0
    while len(line) < n**2 - 1:
        if cnt % 2 == 0:
            step += 1
        for _ in range(step):
            i += di[d]
            j += dj[d]
            if len(line) < n**2 - 1:
                line.append([i, j])
            else:
                break
        d = (d + 1) % 4
        cnt += 1
    return line
 
def grid_to_line(grid):
    res = []
    for i, j in line_idx:
        res.append(grid[i][j])
    return res

def line_to_grid(line):
    res = [[0] * n for _ in range(n)]
    for i in range(len(line)):
        gi, gj = line_idx[i]
        res[gi][gj] = line[i]
    return res

def pull(line):
    for i in reversed(range(len(line))):
        if line[i] == 0:
            line.pop(i)

def boom(line):
    i = 0
    temp = []
    while i < len(line):
        num = line[i]
        cnt = 1
        while i + cnt < len(line) and line[i + cnt] == num:
            cnt += 1
        if cnt >= 4:
            for j in range(cnt):
                temp.append(i + j)
        i += cnt
    score = 0
    for i in reversed(temp):
        num = line.pop(i)
        score += num
    return line, score

def change(line):
    new = []
    i = 0
    while i < len(line):
        num = line[i]
        cnt = 1
        while i + cnt < len(line) and line[i + cnt] == num:
            cnt += 1
        new.extend([cnt, num])
        i += cnt
    return new[:n**2 - 1]

n, m, grid, magic = init()
line_idx = get_line_idx()
score = 0
for d, s in magic:
    blizard(d, s)
    line = grid_to_line(grid)
    pull(line)
    while True:
        line, temp = boom(line)
        score += temp
        if temp == 0:
            break
    line = change(line)
    grid = line_to_grid(line)
print(score)