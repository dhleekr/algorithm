di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def init():
    N, M, K = map(int, input().split())
    fireballs = []
    for _ in range(M):
        i, j, m, s, d = map(int, input().split())
        i -= 1
        j -= 1
        fireballs.append([i, j, m, s, d])
    return N, M, K, fireballs

def move():
    new = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                for _ in range(len(grid[i][j])):
                    m, s, d = grid[i][j].pop()
                    new_i = (i + s * di[d]) % N
                    new_j = (j + s * dj[d]) % N
                    new[new_i][new_j].append([m, s, d])
    return new

def multi_fireballs():
    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) >= 2:
                cnt = len(grid[i][j])
                sum_m = 0
                sum_s = 0
                is_even = False
                is_odd = False
                for _ in range(cnt):
                    m, s, d = grid[i][j].pop()
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:
                        is_even = True
                    else:
                        is_odd = True
                new_m = sum_m // 5
                if new_m == 0:
                    continue
                new_s = sum_s // cnt
                if is_even and is_odd:
                    new_d = [1, 3, 5, 7]
                else:
                    new_d = [0, 2, 4, 6]
                for nd in new_d:
                    grid[i][j].append([new_m, new_s, nd])

N, M, K, fireballs = init()
grid = [[[] for _ in range(N)] for _ in range(N)]
for i, j, m, s, d in fireballs:
    grid[i][j].append([m, s, d])

for _ in range(K):
    grid = move()
    multi_fireballs()

ans = 0
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            ans += sum(row[0] for row in grid[i][j])
print(ans)