def init():
    N, Q = list(map(int, input().split()))

    grid = [list(map(int, input().split())) for _ in range(2**N)]

    L = list(map(int, input().split()))

    return N, grid, L


def rotation(fraction):
    length = len(fraction)
    new_fraction = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            new_fraction[j][length-i-1] = fraction[i][j]

    return new_fraction


def make_fraction_list():
    i = 2**L
    fraction_list = []

    while i <= 2**N:
        j = 2**L
        i_list = []
        for a in range(i - 2**L, i):
            i_list.append(a)
        
        while j <= 2**N:
            j_list = []
            for b in range(j - 2**L, j):
                j_list.append(b)

            fraction_list.append([i_list, j_list])

            j += 2**L
        
        i += 2**L

    return fraction_list


def ice_reduce(grid):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    new_grid = [[0]*2**N for _ in range(2**N)]

    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            for d in range(4):
                new_i = i + di[d]
                new_j = j + dj[d]
                
                if 0 <= new_i < 2**N and 0 <= new_j < 2**N and grid[new_i][new_j] > 0:
                    cnt += 1

            if cnt < 3:
                if grid[i][j] > 0:
                    new_grid[i][j] = grid[i][j] - 1
            else:
                new_grid[i][j] = grid[i][j]
    
    return new_grid


def firestorm(grid, L):
    fraction_list = make_fraction_list()

    for i_list, j_list in fraction_list:
        fraction = [[0]*2**L for _ in range(2**L)]

        a = 0
        for i in i_list:
            b = 0
            for j in j_list:
                fraction[a][b] = grid[i][j]
                b += 1
            a += 1
        
        new_fraction = rotation(fraction)

        a = 0
        for i in i_list:
            b = 0
            for j in j_list:
                grid[i][j] = new_fraction[a][b] 
                b += 1
            a += 1

    grid = ice_reduce(grid)

    return grid


def bfs(grid, i, j):
    q = [(i, j)]
    visited[i][j] = 1
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    if grid[i][j] > 0:
        ans_max = 1
    else:
        ans_max = 0

    while q:
        i, j = q.pop(0)
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]

            if 0 <= new_i < 2**N and 0 <= new_j < 2**N and grid[new_i][new_j] > 0 and not visited[new_i][new_j]: 
                visited[new_i][new_j] = 1
                q.append((new_i, new_j))
                ans_max += 1
    
    return ans_max


N, grid, L_list = init()

for L in L_list:
    grid = firestorm(grid, L)

ans = 0
max_ans = 0
for i in range(len(grid)):
    ans += sum(grid[i])

visited = [[0]*2**N for _ in range(2**N)]

max_ans = 0

for i in range(2**N):
    for j in range(2**N):
        if not visited[i][j]:
            ans_max = bfs(grid, i, j)
            if max_ans < ans_max:
                max_ans = ans_max

print(ans)
print(max_ans)