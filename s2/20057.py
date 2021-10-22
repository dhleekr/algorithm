def init():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    return N, grid

def tornado_pos():
    i, j = N//2, N//2
    index = [[0]] * N**2
    index[0] = [i, j, -1]
    d = 0
    dist = 0
    cnt = 0
    while cnt < N**2-1:
        if d % 2 == 0:
            dist += 1
        for s in range(dist):
            cnt += 1
            i = i + di[d]
            j = j + dj[d]
            index[cnt] = [i, j, d]

            if cnt == N**2 - 1:
                break

        d = (d+1) % 4

    return index

def wind(pos):
    i, j, d = pos
    total = grid[i][j]
    lose = 0
    score = 0
    if 0 <= i + 2*di[d] < N and 0 <= j + 2*dj[d] < N:
        grid[i + 2*di[d]][j + 2*dj[d]] += int(0.05*grid[i][j])
    else:
        score += int(0.05*grid[i][j])
    lose += int(0.05*grid[i][j])

    if 0 <= i+di[d]+di[(d+3)%4] < N and 0 <= j+dj[d]+dj[(d+3)%4] < N:
        grid[i + di[d] + di[(d+3)%4]][j + dj[d] + dj[(d+3)%4]] += int(0.1*grid[i][j])
    else:
        score += int(0.1*grid[i][j])
    lose += int(0.1*grid[i][j])

    if 0 <= i + di[d] + di[(d + 1) % 4] < N and 0 <= j + dj[d] + dj[(d + 1) % 4] < N:
        grid[i + di[d] + di[(d + 1) % 4]][j + dj[d] + dj[(d + 1) % 4]] += int(0.1 * grid[i][j])
    else:
        score += int(0.1*grid[i][j])
    lose += int(0.1 * grid[i][j])

    if 0 <= i+di[(d+3)%4] < N and 0 <= j+dj[(d+3)%4] < N:
        grid[i + di[(d+3)%4]][j + dj[(d+3)%4]] += int(0.07*grid[i][j])
    else:
        score += int(0.07*grid[i][j])
    lose += int(0.07*grid[i][j])

    if 0 <= i + 2*di[(d + 3) % 4] < N and 0 <= j + 2*dj[(d + 3) % 4] < N:
        grid[i + 2*di[(d + 3) % 4]][j + 2*dj[(d + 3) % 4]] += int(0.02 * grid[i][j])
    else:
        score += int(0.02*grid[i][j])
    lose += int(0.02 * grid[i][j])

    if 0 <= i + di[(d + 1) % 4] < N and 0 <= j + dj[(d + 1) % 4] < N:
        grid[i + di[(d + 1) % 4]][j + dj[(d + 1) % 4]] += int(0.07 * grid[i][j])
    else:
        score += int(0.07*grid[i][j])
    lose += int(0.07 * grid[i][j])

    if 0 <= i + 2 * di[(d + 1) % 4] < N and 0 <= j + 2 * dj[(d + 1) % 4] < N:
        grid[i + 2 * di[(d + 1) % 4]][j + 2 * dj[(d + 1) % 4]] += int(0.02 * grid[i][j])
    else:
        score += int(0.02*grid[i][j])
    lose += int(0.02 * grid[i][j])

    if 0 <= i + di[(d + 2) % 4] + di[(d + 3) % 4] < N and 0 <= j + dj[(d + 2) % 4] + dj[(d + 3) % 4] < N:
        grid[i + di[(d + 2) % 4] + di[(d + 3) % 4]][j + dj[(d + 2) % 4] + dj[(d + 3) % 4]] += int(0.01 * grid[i][j])
    else:
        score += int(0.01*grid[i][j])
    lose += int(0.01 * grid[i][j])

    if 0 <= i + di[(d + 2) % 4] + di[(d + 1) % 4] < N and 0 <= j + dj[(d + 2) % 4] + dj[(d + 1) % 4] < N:
        grid[i + di[(d + 2) % 4] + di[(d + 1) % 4]][j + dj[(d + 2) % 4] + dj[(d + 1) % 4]] += int(0.01 * grid[i][j])
    else:
        score += int(0.01*grid[i][j])
    lose += int(0.01 * grid[i][j])

    if 0 <= i+di[d] < N and 0 <= j+dj[d] < N:
        grid[i + di[d]][j + dj[d]] += total-lose
    else:
        score += total-lose
    grid[i][j] = 0

    return score



di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

N, grid = init()
index = tornado_pos()
total_score = 0
for pos in index[1:]:
    score = wind(pos)
    total_score += score

print(total_score)