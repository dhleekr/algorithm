def init():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    ds_list = []
    for _ in range(M):
        ds_list.append(list(map(int, input().split())))

    return N, M, grid, ds_list

def move(cloud_list, ds, visited):
    d = ds[0]-1
    s = ds[1]
    new = []
    for (i, j) in cloud_list:
        new_i = (i + s*di[d]) % N
        new_j = (j + s*dj[d]) % N
        visited[new_i][new_j] = 1
        grid[new_i][new_j] += 1
        new.append([new_i, new_j])

    return new

def copy(cloud_list):
    for (i, j) in cloud_list:
        cnt = 0
        for d in range(1, 8, 2):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < N and 0 <= new_j < N and grid[new_i][new_j] >= 1:
                cnt += 1

        grid[i][j] += cnt

def make_cloud(visited):
    cloud_list = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and grid[i][j] >= 2:
                cloud_list.append([i, j])
                grid[i][j] -= 2

    return cloud_list

def magic():
    for i in range(M):
        if i == 0:
            cloud_list = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
        ds = ds_list[i]
        visited = [[0]*N for _ in range(N)]
        cloud_list = move(cloud_list, ds, visited)
        copy(cloud_list)
        cloud_list = make_cloud(visited)


di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M, grid, ds_list = init()
magic()
print(sum(sum(row) for row in grid))