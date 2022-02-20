di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
s_di = [-1, 0, 1, 0]
s_dj = [0, -1, 0, 1]

def init():
    m, s = map(int, input().split())
    fish_info = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    shark = list(map(lambda x: int(x) - 1, input().split()))
    return m, s, fish_info, shark

def move_fish(grid):
    new = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            while grid[i][j]:
                d = grid[i][j].pop()
                for nd in range(d, d - 8, -1):
                    nd %= 8
                    new_i = i + di[nd]
                    new_j = j + dj[nd]
                    if [new_i, new_j] != shark and 0 <= new_i < 4 and 0 <= new_j < 4 and smell_map[new_i][new_j] == 0:
                        new[new_i][new_j].append(nd)
                        break
                else:
                    new[i][j].append(d)
    return new

def move_shark(shark):
    si, sj = shark
    res = []
    for i in range(4):
        new_si1 = si + s_di[i]
        new_sj1 = sj + s_dj[i]
        if 0 <= new_si1 < 4 and 0 <= new_sj1 < 4:
            for j in range(4):
                new_si2 = new_si1 + s_di[j]
                new_sj2 = new_sj1 + s_dj[j]
                if 0 <= new_si2 < 4 and 0 <= new_sj2 < 4:
                    for k in range(4):
                        visited = [[0] * 4 for _ in range(4)]
                        new_si3 = new_si2 + s_di[k]
                        new_sj3 = new_sj2 + s_dj[k]
                        if 0 <= new_si3 < 4 and 0 <= new_sj3 < 4:
                            route = [[new_si1, new_sj1], [new_si2, new_sj2], [new_si3, new_sj3]]
                            c = str(i+1) + str(j+1) + str(k+1)
                            if (new_si3, new_sj3) != (new_si1, new_sj1):
                                cnt = len(temp[new_si1][new_sj1]) + len(temp[new_si2][new_sj2]) + len(temp[new_si3][new_sj3])
                            else:
                                cnt = len(temp[new_si1][new_sj1]) + len(temp[new_si2][new_sj2])
                            res.append([cnt, -int(c), route])
                    
    res.sort(reverse=True, key=lambda x: (x[0], x[1]))
    cnt, _, route = res[0]
    for i, j in route:
        if temp[i][j]:
            temp[i][j] = []
            smell_map[i][j] = 3
    return route[-1]   


m, s, fish_info, shark = init()
grid = [[[] for _ in range(4)] for _ in range(4)]
smell_map = [[0] * 4 for _ in range(4)]

for i, j, d in fish_info:
    grid[i][j].append(d)

for _ in range(s):
    temp = [[f[:] for f in row] for row in grid]
    temp = move_fish(temp)
    shark = move_shark(shark)

    for i in range(4):
        for j in range(4):
            if smell_map[i][j]:
                smell_map[i][j] -= 1

    for i in range(4):
        for j in range(4):
            grid[i][j] += temp[i][j]

print(sum(sum(len(f) for f in row) for row in grid))