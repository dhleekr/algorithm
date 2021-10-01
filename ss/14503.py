def init():
    N, M = map(int, input().split())
    robot = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]

    return N, M, robot, grid

def clean(robot):
    while True:
        i, j, d = robot
        visited[i][j] = 1
        work = False

        for _ in range(4):
            d = (d+3) % 4
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < N and 0 <= new_j < M and not visited[new_i][new_j] and grid[new_i][new_j] != 1:
                robot = [new_i, new_j, d]
                visited[new_i][new_j] = 1
                work = True
                break

        if not work:
            d = (d+2) % 4
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < N and 0 <= new_j < M and grid[new_i][new_j] != 1:
                robot = [new_i, new_j, (d+2)%4]
            else:
                break


N, M, robot, grid = init()
visited = [[0]*M for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

clean(robot)
print(sum(sum(row) for row in visited))