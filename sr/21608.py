di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n = int(input())
    favorites = {}
    for _ in range(n**2):
        temp = list(map(int, input().split()))
        favorites[temp[0]] = temp[1:]
    return n, favorites

def seat(num):
    temp = []
    for i in range(n):
        for j in range(n):
            f_cnt = 0
            e_cnt = 0
            if grid[i][j] == 0:
                for d in range(4):
                    new_i = i + di[d]
                    new_j = j + dj[d]
                    if 0 <= new_i < n and 0 <= new_j < n:
                        if grid[new_i][new_j] in favorites[num]:
                            f_cnt += 1
                        if grid[new_i][new_j] == 0:
                            e_cnt += 1
                temp.append([f_cnt, e_cnt, i, j])
    temp.sort(reverse=True, key=lambda x : (x[0], x[1], -x[2], -x[3]))
    return temp[0][2:]

def satisfy():
    score = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for d in range(4):
                new_i = i + di[d]
                new_j = j + dj[d]
                if 0 <= new_i < n and 0 <= new_j < n:
                    if grid[new_i][new_j] in favorites[grid[i][j]]:
                        cnt += 1
            if cnt != 0:
                score += 10 ** (cnt - 1)
    return score

n, favorites = init()
grid = [[0] * n for _ in range(n)]

for num in favorites.keys():
    i, j = seat(num)
    grid[i][j] = num

print(satisfy())