def init():
    N, M, K = map(int, input().split())
    shark_map = [list(map(int, input().split())) for _ in range(N)]

    direction_init = list(map(int, input().split()))

    priority = []

    for i in range(M):
        shark = []
        for j in range(4):
            temp = list(map(int, input().split()))
            shark.append(temp)
        priority.append(shark)

    for i in range(M):
        direction_init[i] -= 1
        for j in range(4):
            for k in range(4):
                priority[i][j][k] -= 1

    smell_map = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            shark = shark_map[i][j]
            if shark != 0:
                shark_map[i][j] = [shark, direction_init[shark-1]]
                smell_map[i][j] = [shark, K]

    return N, M, K, shark_map, smell_map, priority

def find_shark():
    idx = []
    for i in range(N):
        for j in range(N):
            if shark_map[i][j] != 0:
                idx.append([i, j])
    return idx

def smell_update():
    for i in range(N):
        for j in range(N):
            if smell_map[i][j] != 0:
                if smell_map[i][j][1] > 0:
                    smell_map[i][j][1] -= 1
                    if smell_map[i][j][1] == 0:
                        smell_map[i][j] = 0
                

    return smell_map

def shark_move():
    shark_idx = find_shark()

    update = []
    for idx in shark_idx:
        i, j = idx
        shark = shark_map[i][j][0]
        current_d = shark_map[i][j][1]

        d_list = priority[shark-1][current_d]
        done = False

        for d in d_list:
            new_i = i + di[d]
            new_j = j + dj[d]

            if 0 <= new_i < N and 0 <= new_j < N and smell_map[new_i][new_j] == 0 and shark_map[new_i][new_j] == 0:
                update.append([i, j, new_i, new_j, shark, d])
                done = True
                break
        if done:
            continue     

        for d in d_list:
            new_i = i + di[d]
            new_j = j + dj[d]

            if  0 <= new_i < N and 0 <= new_j < N and smell_map[new_i][new_j][0] == shark:
                update.append([i, j, new_i, new_j, shark, d])
                done = True
                break
        if done:
            continue

    smell_update()
    for u in update:
        i, j, new_i, new_j, shark, d = u
        if shark_map[new_i][new_j] != 0:
            if shark < shark_map[new_i][new_j][0]:
                shark_map[new_i][new_j], shark_map[i][j] = [shark, d], 0
                smell_map[new_i][new_j] = [shark, K]
            else:
                shark_map[i][j] = 0
        else:
            shark_map[new_i][new_j], shark_map[i][j] = [shark, d], 0
            smell_map[new_i][new_j] = [shark, K]

N, M, K, shark_map, smell_map, priority = init()

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

t = 0
while True:
    shark_move()
    t += 1

    idx = find_shark()
    if len(idx) == 1:
        break

    if t >= 1000:
        t = -1
        break

print(t)