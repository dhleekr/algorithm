di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    horse = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    return n, m, grid, horse

def find_idx(a):
    for i in range(n):
        for j in range(n):
            for k in range(len(chess[i][j])):
                if chess[i][j][k][0] == a:
                    return [i, j, k]

def num_check():
    for i in range(n):
        for j in range(n):
            if len(chess[i][j]) >= 4:
                return True
    return False

def turn():
    for num in range(m):
        i, j, k = find_idx(num)
        d = chess[i][j][k][1]
        new_i = i + di[d]
        new_j = j + dj[d]

        if not(0 <= new_i < n and 0 <= new_j < n) or grid[new_i][new_j] == 2:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2

        chess[i][j][k][1] = d
        new_i = i + di[d]
        new_j = j + dj[d]
        if 0 <= new_i < n and 0 <= new_j < n:
            if grid[new_i][new_j] == 0:
                length = len(chess[i][j][k:])
                for _ in range(length):
                    chess[new_i][new_j].append(chess[i][j].pop(k))
            elif grid[new_i][new_j] == 1:
                length = len(chess[i][j][k:])
                for _ in range(length):
                    chess[new_i][new_j].append(chess[i][j].pop())
        
        if num_check():
            return False
    return True

n, m, grid, horse = init()
chess = [[[] for _ in range(n)] for _ in range(n)]
for idx, h in enumerate(horse):
    i, j, d = h
    chess[i][j].append([idx, d])

for i in range(1000):
    flag = turn()
    if not flag:
        break
if i < 999:
    print(i + 1)
else:
    print(-1)