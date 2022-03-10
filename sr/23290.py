di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
sdi = [-1, 0, 1, 0]
sdj = [0, -1, 0, 1]

def init():
    m, s = map(int, input().split())
    grid = [[[] for _ in range(4)] for _ in range(4)]
    for _ in range(m):
        i, j, d = map(lambda x : int(x) - 1, input().split())
        grid[i][j].append(d)
    shark = list(map(lambda x : int(x) - 1, input().split()))
    return m, s, grid, shark

def deepcopy(grid):
    new = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new[i][j] = grid[i][j][:]
    return new

def fish_move():
    new = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            temp = []
            while grid[i][j]:
                d = grid[i][j].pop()
                cnt = 0
                while True:
                    new_i = i + di[d]
                    new_j = j + dj[d]
                    if 0 <= new_i < 4 and 0 <= new_j < 4 and [new_i, new_j] != shark and fishsmell[new_i][new_j] == 0:
                        new[new_i][new_j].append(d)
                        break
                    else:
                        d = (d - 1) % 8
                        cnt += 1

                    if cnt == 8:
                        new[i][j].append(d)
                        break
    return new

def dfs(i, j, total, traj, depth):
    if depth == 3:
        res.append([total, traj])
        return
    
    for d in range(4):
        new_i = i + sdi[d]
        new_j = j + sdj[d]
        if 0 <= new_i < 4 and 0 <= new_j < 4:
            if grid[new_i][new_j]:
                temp = deepcopy(grid)
                temp[new_i][new_j] = []
                if visited[new_i][new_j] == 0:
                    visited[new_i][new_j] = 1
                    dfs(new_i, new_j, total + len(grid[new_i][new_j]), traj + str(d), depth + 1)
                    visited[new_i][new_j] = 0
                else:
                    dfs(new_i, new_j, total, traj + str(d), depth + 1)
            else:
                dfs(new_i, new_j, total, traj + str(d), depth + 1)

def smell(traj):
    si, sj = shark
    for i in range(len(traj)):
        d = int(traj[i])
        si += sdi[d]
        sj += sdj[d]
        if grid[si][sj]:
            grid[si][sj] = []
            fishsmell[si][sj] = 3
    return [si, sj]

m, s, grid, shark = init()
fishsmell = [[0] * 4 for _ in range(4)]


for _ in range(s):
    copied_grid = deepcopy(grid)
    grid = fish_move()

    visited = [[0] * 4 for _ in range(4)]
    res = []
    dfs(shark[0], shark[1], 0, '', 0)
    res.sort(key=lambda x: (-x[0], x[1]))

    shark = smell(res[0][1])

    for i in range(4):
        for j in range(4):
            if fishsmell[i][j]:
                fishsmell[i][j] -= 1
    
    for i in range(4):
        for j in range(4):
            if copied_grid[i][j]:
                grid[i][j].extend(copied_grid[i][j])

ans = 0
for i in range(4):
    for j in range(4):
        if grid[i][j]:
            ans += len(grid[i][j])
print(ans)