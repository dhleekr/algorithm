n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
moves = []
for i in range(m):
    tmp = list(map(int, input().split()))
    moves.append(tmp)

directions = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7:(1, 0), 8:(1, -1)}
clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

for i in range(m):
    move = moves[i]
    next_clouds = []
    for cloud in clouds:
        x = cloud[0]
        y = cloud[1]
        d = move[0]
        s = move[1]

        x_next = (x + directions[d][0] * s) % n
        y_next = (y + directions[d][1] * s) % n
        next_clouds.append([x_next, y_next])

    visited = [[False]*n for _ in range(n)]
    for cloud in next_clouds:
        x = cloud[0]
        y = cloud[1]
        arr[x][y] += 1
        visited[x][y] = True


    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for cloud in next_clouds:
        x = cloud[0]
        y = cloud[1]
        cnt = 0

        for i in range(4):
            x_diagonal = x + cx[i]
            y_diagoanl = y + cy[i]

            if 0 <= x_diagonal < n and 0 <= y_diagoanl < n and arr[x_diagonal][y_diagoanl] >= 1:
                cnt += 1

        arr[x][y] += cnt


    clouds = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and visited[i][j] == False:
                arr[i][j] -= 2
                clouds.append([i, j])

ans = 0 
for i in range(n):
    ans += sum(arr[i])

print(ans)