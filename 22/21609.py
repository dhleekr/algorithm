def init():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    return N, M, grid

def rotate(grid):
    new_grid = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[N-j-1][i] = grid[i][j]
    return new_grid

def gravity():
    for i in reversed(range(N-1)):
        for j in range(N):
            if grid[i][j] > -1:
                row = i
                while True:
                    if row+1 < N and grid[row+1][j] == -2:
                        grid[row+1][j] = grid[row][j]
                        grid[row][j] = -2
                        row += 1
                    else:
                        break

def bfs(i, j, color):
    q = [[i, j]]
    block_cnt, rainbow = 1, 0
    blocks, rainbows = [[i,j]], []

    while q:
        i, j = q.pop(0)
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]

            if 0 <= new_i < N and 0 <= new_j < N and not visited[new_i][new_j] \
                and grid[new_i][new_j] == color:
                visited[new_i][new_j] = 1
                q.append([new_i, new_j])
                block_cnt += 1
                blocks.append([new_i, new_j])
            
            elif 0 <= new_i < N and 0 <= new_j < N and not visited[new_i][new_j] \
                and grid[new_i][new_j] == 0:
                visited[new_i][new_j] = 1
                q.append([new_i, new_j])
                block_cnt += 1
                rainbow += 1
                rainbows.append([new_i, new_j])
    
    for i, j in rainbows:
        visited[i][j] = 0
    
    return [block_cnt, rainbow, blocks+rainbows]


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M, grid = init()
score = 0

while True:
    visited = [[0]*N for _ in range(N)]
    blocks = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                block_info = bfs(i, j, grid[i][j])

                if block_info[0] > 1:
                    blocks.append(block_info)

    if not blocks:
        break
    blocks.sort(reverse=True)

    # Delete
    for (i, j) in blocks[0][2]:
        grid[i][j] = -2
        
    score += blocks[0][0]**2

    gravity()
    grid = rotate(grid)
    gravity()

print(score)