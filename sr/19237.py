di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def init():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    shark_dir = list(map(lambda x : int(x) - 1, input().split()))
    priority = []
    for _ in range(m):
        temp = []
        for _ in range(4):
            temp.append(list(map(lambda x : int(x) - 1, input().split())))
        priority.append(temp)
    return n, m, k, grid, shark_dir, priority

def find_idx():
    res = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                res.append([grid[i][j] - 1, i, j])
    return res

def deepcopy(arr):
    return [[b[:] for b in a] for a in arr]

def move():
    new_shark_loc = dict()
    new_smell_map = deepcopy(smell_map)

    for i, j in shark_loc.keys():
        num, d = shark_loc[(i, j)]
        for nd in priority[num][d]:
            new_i = i + di[nd]
            new_j = j + dj[nd]
            if 0 <= new_i < n and 0 <= new_j < n and smell_map[new_i][new_j] == [-1, 0]: # 아무냄새 없을때
                if new_smell_map[new_i][new_j] == [-1, 0]:
                    new_smell_map[new_i][new_j] = [num, k + 1]
                    new_shark_loc[(new_i, new_j)] = [num, nd]
                else:
                    if num < new_smell_map[new_i][new_j][0]:
                        new_smell_map[new_i][new_j] = [num, k + 1]
                        new_shark_loc[(new_i, new_j)] = [num, nd]
                break   
        else:
            for nd in priority[num][d]:
                new_i = i + di[nd]
                new_j = j + dj[nd]
                if 0 <= new_i < n and 0 <= new_j < n and smell_map[new_i][new_j][0] == num: # 자기 냄새
                    new_smell_map[new_i][new_j] = [num, k + 1]
                    new_shark_loc[(new_i, new_j)] = [num, nd]
                    break
    
    return new_shark_loc, new_smell_map

def smell_fly():
    for i in range(n):
        for j in range(n):
            if smell_map[i][j] != [-1, 0]: # [상어 번호, 남은 시간]
                num, temp = smell_map[i][j]
                temp -= 1
                if temp == 0:
                    smell_map[i][j] = [-1, 0]
                else:
                    smell_map[i][j] = [num, temp]

n, m, k, grid, shark_dir, priority = init()
smell_map = [[[-1, 0] for _ in range(n)] for _ in range(n)]
shark_loc = dict()

for temp in find_idx():
    num, i, j = temp
    d = shark_dir[num]
    shark_loc[(i, j)] = [num, d]
    smell_map[i][j] = [num, k]

t = 0
while len(shark_loc.keys()) > 1:
    t += 1
    shark_loc, smell_map = move()
    smell_fly()
    if t > 1000:
        t = -1
        break
print(t)