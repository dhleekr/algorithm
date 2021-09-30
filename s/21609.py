def group_block(i, j, color):
    temp = []
    temp.append([i, j])
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    block_cnt, rainbow_cnt = 1, 0
    blocks, rainbows = [[i, j]], []

    while temp:
        i, j = temp.pop(0)
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]

            if 0 <= new_i < N and 0 <= new_j < N and not visited[new_i][new_j] and grid[new_i][new_j] == color:
                visited[new_i][new_j] = 1
                temp.append([new_i, new_j])
                block_cnt += 1
                blocks.append([new_i, new_j])
            
            elif 0 <= new_i < N and 0 <= new_j < N and not visited[new_i][new_j] and grid[new_i][new_j] == 0:
                visited[new_i][new_j] = 1
                temp.append([new_i, new_j])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([new_i, new_j])

    for i, j in rainbows:
        visited[i][j] = 0

    return [block_cnt, rainbow_cnt, blocks+rainbows]

def del_blocks(blocks):
    for i, j in blocks:
        grid[i][j] = -2

def gravity(grid):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if grid[i][j] > -1:
                row = i
                while True:
                    if 0 <= row+1 < N and grid[row+1][j] == -2:
                        grid[row+1][j] = grid[row][j]
                        grid[row][j] = -2
                        row += 1
                    else:
                        break

def rotation(grid):
    new_grid = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[N-1-j][i] = grid[i][j]
    return new_grid

N, M = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]

ans = 0

while True:
    visited = [[0]*N for _ in range(N)]
    blocks = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                block_info = group_block(i, j, grid[i][j])

                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)

    if not blocks:
        break

    del_blocks(blocks[0][2])
    ans += blocks[0][0]**2

    gravity(grid)

    grid = rotation(grid)

    gravity(grid)

print(ans)