di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

def init():
    r, c, m = map(int, input().split())
    shark = []
    for _ in range(m):
        i, j, s, d, z = map(int, input().split())
        i -= 1
        j -= 1
        d -= 1
        shark.append([i, j, s, d, z])
    return r, c, m, shark

def move():
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] != 0:
                si, sj = i, j
                s, d, z = grid[i][j]
                while s > 0:
                    si += di[d]
                    sj += dj[d]
                    if 0 <= si < r and 0 <= sj < c:
                        s -= 1
                    else:
                        si -= di[d]
                        sj -= dj[d]
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2
                if temp[si][sj] == 0:
                    temp[si][sj] = [grid[i][j][0], d, z]
                else:
                    if temp[si][sj][2] < z:
                        temp[si][sj] = [grid[i][j][0], d, z]
    return temp
        
r, c, m, shark = init()
grid = [[0] * c for _ in range(r)]
for temp in shark:
    i, j, s, d, z = temp
    grid[i][j] = [s, d, z]

total = 0
for j in range(c):
    for i in range(r):
        if grid[i][j] != 0:
            total += grid[i][j][2]
            grid[i][j] = 0
            break
    grid = move()

print(total)