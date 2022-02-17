di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    r, c, k = map(int, input().split())
    heater_list = []
    check_list = []
    for i in range(r):
        temp = list(map(int, input().split()))
        for j in range(c):
            if temp[j] == 5:
                check_list.append([i, j])
            elif temp[j] != 0:
                heater_list.append([i, j, temp[j]])
    w = int(input())
    walls = [[[0, 0] for _ in range(c)] for _ in range(r)]
    for _ in range(w):
        x, y, wall = map(int, input().split())
        x -= 1
        y -= 1
        walls[x][y][wall] = 1
    return r, c, k, heater_list, check_list, w, walls

def dfs(i, j, direction, depth):
    if depth == 5:
        return
    if direction == 1:
        if depth == 1:
            j += 1
            visited[i][j] = 1
            heat_map[i][j] += 5

        for idx, temp in enumerate([[-1, 1], [0, 1], [1, 1]]):
            new_i = i + temp[0]
            new_j = j + temp[1]
            if 0 <= new_i < r and 0 <= new_j < c:
                if idx == 0:
                    if walls[i][j][0] == 0 and walls[new_i][j][1] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
                elif idx == 1:
                    if walls[i][j][1] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
                elif idx == 2:
                    if walls[new_i][j][0] == 0 and walls[new_i][j][1] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
    elif direction == 2:
        if depth == 1:
            j -= 1
            visited[i][j] = 1
            heat_map[i][j] += 5

        for idx, temp in enumerate([[-1, -1], [0 , -1], [1, -1]]):
            new_i = i + temp[0]
            new_j = j + temp[1]
            if 0 <= new_i < r and 0 <= new_j < c:
                if idx == 0:
                    if walls[i][j][0] == 0 and walls[new_i][new_j][1] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
                elif idx == 1:
                    if walls[i][new_j][1] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
                else:
                    if walls[new_i][new_j][1] == 0 and walls[new_i][j][0] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
    elif direction == 3:
        if depth == 1:
            i -= 1
            visited[i][j] = 1
            heat_map[i][j] += 5

        for idx, temp in enumerate([[-1, -1], [-1, 0], [-1, 1]]):
            new_i = i + temp[0]
            new_j = j + temp[1]
            if 0 <= new_i < r and 0 <= new_j < c:
                if idx == 0:
                    if walls[i][new_j][0] == 0 and walls[i][new_j][1] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
                elif idx == 1:
                    if walls[i][j][0] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
                else:
                    if walls[i][j][1] == 0 and walls[i][new_j][0] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
    elif direction == 4:
        if depth == 1:
            i += 1
            visited[i][j] = 1
            heat_map[i][j] += 5

        for idx, temp in enumerate([[1, -1], [1, 0], [1, 1]]):
            new_i = i + temp[0]
            new_j = j + temp[1]
            if 0 <= new_i < r and 0 <= new_j < c:
                if idx == 0:
                    if walls[new_i][new_j][0] == 0 and walls[i][new_j][1] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
                elif idx == 1:
                    if walls[new_i][j][0] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)
                else:
                    if walls[i][j][1] == 0 and walls[new_i][new_j][0] == 0 and visited[new_i][new_j] == 0:
                        visited[new_i][new_j] = 1
                        heat_map[new_i][new_j] += 5 - depth
                        dfs(new_i, new_j, direction, depth + 1)

def temp_control():
    visited = [[0] * c for _ in range(r)]
    new = []
    for i in range(r):
        new.append(heat_map[i][:])

    for i in range(r):
        for j in range(c):
            visited[i][j] = 1
            for d in range(4):
                new_i = i + di[d]
                new_j = j + dj[d]
                if 0 <= new_i < r and 0 <= new_j < c and visited[new_i][new_j] == 0:
                    if d == 0 and walls[i][j][1] == 1: # [오, 아, 왼, 위]
                        continue
                    elif d == 1 and walls[new_i][j][0] == 1:
                        continue
                    elif d == 2 and walls[i][new_j][1] == 1:
                        continue
                    elif d == 3 and walls[i][j][0] == 1:
                        continue
                    if heat_map[i][j] > heat_map[new_i][new_j]:
                        temp = (heat_map[i][j] - heat_map[new_i][new_j]) // 4
                        new[i][j] -= temp
                        new[new_i][new_j] += temp
                    elif heat_map[i][j] < heat_map[new_i][new_j]:
                        temp = (heat_map[new_i][new_j] - heat_map[i][j]) // 4
                        new[i][j] += temp
                        new[new_i][new_j] -= temp
    return new

r, c, k, heater_list, check_list, w, walls = init()
heat_map = [[0] * c for _ in range(r)]
cnt = 0
while cnt < 101:
    check = True
    for heater in heater_list:
        visited = [[0] * c for _ in range(r)]
        dfs(heater[0], heater[1], heater[2], 1)

    heat_map = temp_control()

    for j in range(c):
        if heat_map[0][j] >= 1:
            heat_map[0][j] -= 1
        if heat_map[r - 1][j] >= 1:
            heat_map[r - 1][j] -= 1
    for i in range(1, r - 1):
        if heat_map[i][0] >= 1:
            heat_map[i][0] -= 1
        if heat_map[i][c - 1] >= 1:
            heat_map[i][c - 1] -= 1
    cnt += 1
    for i, j in check_list:
        if heat_map[i][j] < k:
            check = False
    if check:
        break

print(cnt)