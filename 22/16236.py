di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n = int(input())
    grid = []
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            if temp[j] == 9:
                shark = [i, j]
                temp[j] = 2
        grid.append(temp)
        
    return n, grid, shark

def bfs(shark):
    i, j = shark
    q = [[i, j, 0]]
    eat = []
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1 
    while q:
        i, j, dist = q.pop(0)
        dist += 1
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] <= grid[shark[0]][shark[1]] and visited[new_i][new_j] == 0:
                visited[new_i][new_j] = 1
                q.append([new_i, new_j, dist])
                if 0 < grid[new_i][new_j] < grid[shark[0]][shark[1]]:
                    eat.append([new_i, new_j, dist])

    if not eat:
        return None
    eat.sort(key=lambda x: (x[2], x[0], x[1]))
    return eat[0]


n, grid,shark = init()

ans = 0
cnt = 0

fish = bfs(shark)
while fish:
    i, j, dist = fish
    cnt += 1
    ans += dist
    size = grid[shark[0]][shark[1]]
    if cnt == size:
        grid[i][j] = size + 1
        grid[shark[0]][shark[1]] = 0
        cnt = 0
    else:
        grid[i][j] = size
        grid[shark[0]][shark[1]] = 0
    shark = [i, j]
    fish = bfs(shark)
print(ans)