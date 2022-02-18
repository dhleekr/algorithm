di = [0, 1, 0, -1] # 동 남 서 북
dj = [1, 0, -1, 0]

def init():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, k, grid

def get_score(i, j):
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    q = [[i, j]]
    temp = grid[i][j]
    cnt = 1
    while q:
        i, j = q.pop(0)
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < n and 0 <= new_j < m and visited[new_i][new_j] == 0 and grid[new_i][new_j] == temp:
                visited[new_i][new_j] = 1
                q.append([new_i, new_j])
                cnt += 1

    return cnt * temp

def solve(i, j, d):
    global score
    for _ in range(k):
        if not(0 <= i + di[d] < n and 0 <= j + dj[d] < m):
            d = (d + 2) % 4
        i += di[d]
        j += dj[d]
        
        if d == 0:
            dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
        elif d == 1:
            dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]
        elif d == 2:
            dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
        else:
            dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]

        if dice[5] > grid[i][j]:
            d = (d + 1) % 4
        elif dice[5] < grid[i][j]:
            d = (d - 1) % 4

        score += get_score(i, j)


n, m, k, grid = init()
dice = [1, 2, 3, 4, 5, 6]
score = 0
solve(0, 0, 0)
print(score)