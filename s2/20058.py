def init():
    N, Q = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(2**N)]
    L = map(int, input().split())

    return N, Q, grid, L

def rotation(mini):
    length = len(mini)
    new = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            new[j][length-1-i] = mini[i][j]

    return new

def icebraeak(grid):
    copy = deepcopy(grid)
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            if grid[i][j] > 0:
                for d in range(4):
                    new_i = i + di[d]
                    new_j = j + dj[d]
                    if 0 <= new_i < 2**N and 0 <= new_j < 2**N and grid[new_i][new_j] > 0:
                        cnt += 1

                if cnt < 3:
                    copy[i][j] -= 1

    return copy

def fire_storm(L):
    for i in range(0, 2**N, 2**L):
        for j in range(0, 2**N, 2**L):
            mini = [row[j:j+2**L] for row in grid[i:i+2**L]]
            new = rotation(mini)
            for idx1 in range(len(new)):
                for idx2 in range(len(new)):
                    grid[i+idx1][j+idx2] = new[idx1][idx2]

def deepcopy(grid):
    new_grid = []
    for i in range(2**N):
        new_grid.append(grid[i][:])
    return new_grid

def bfs():
    max_block = 0
    for i in range(2**N):
        for j in range(2**N):
            if visited[i][j] == 0 and grid[i][j] > 0:
                visited[i][j] = 1
                q = [[i, j]]
                block = 1
                while q:
                    i, j = q.pop(0)
                    for d in range(4):
                        new_i = i + di[d]
                        new_j = j + dj[d]
                        if 0 <= new_i < 2**N and 0 <= new_j < 2**N and grid[new_i][new_j] > 0 and visited[new_i][new_j] == 0:
                            visited[new_i][new_j] = 1
                            q.append([new_i, new_j])
                            block += 1

                max_block = max(max_block, block)

    return max_block


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, Q, grid, L_list = init()
for L in L_list:
    if L > 0:
        fire_storm(L)
    grid = icebraeak(grid)

visited = [[0]*2**N for _ in range(2**N)]
max_block = bfs()
print(sum(sum(row) for row in grid))
print(max_block)