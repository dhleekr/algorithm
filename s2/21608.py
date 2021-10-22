def init():
    N = int(input())
    temp = [list(map(int, input().split())) for _ in range(N**2)]

    students = {}
    for i in range(N**2):
        students[temp[i][0]] = temp[i][1:]

    return N, students

def select_seat(s):
    favorite = students[s]
    info = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                favorite_cnt = 0
                empty_cnt = 0
                for d in range(4):
                    new_i = i + di[d]
                    new_j = j + dj[d]

                    if 0 <= new_i < N and 0 <= new_j < N:
                        if grid[new_i][new_j] in favorite:
                            favorite_cnt += 1
                        if grid[new_i][new_j] == 0:
                            empty_cnt += 1

                info.append([favorite_cnt, empty_cnt, i, j])
    info.sort(reverse=True, key=lambda x: [x[0], x[1], -x[2], -x[3]])

    return info[0]

def satisfy():
    score = 0
    for i in range(N):
        for j in range(N):
            s = grid[i][j]
            favorite = students[s]
            cnt = 0
            for d in range(4):
                new_i = i + di[d]
                new_j = j + dj[d]
                if 0 <= new_i < N and 0 <= new_j < N and grid[new_i][new_j] in favorite:
                    cnt += 1

            if cnt == 1:
                score += 1
            elif cnt == 2:
                score += 10
            elif cnt == 3:
                score += 100
            elif cnt == 4:
                score += 1000

    return score


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, students = init()
grid = [[0]*N for _ in range(N)]

for i in students.keys():
    info = select_seat(i)
    grid[info[2]][info[3]] = i

print(satisfy())