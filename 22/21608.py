di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def solve(s):
    res = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                favorite = 0
                empty = 0
                for d in range(4):
                    new_i = i + di[d]
                    new_j = j + dj[d]
                    if 0 <= new_i < n and 0 <= new_j < n:
                        if grid[new_i][new_j] == 0:
                            empty += 1
                        elif grid[new_i][new_j] in students[s]:
                            favorite += 1
                res.append([favorite, empty, i , j])
    res.sort(reverse=True, key=lambda x: (x[0], x[1], -x[2], -x[3]))
    return res[0][2:]

# 입력 받기
n = int(input())
students = dict()
for _ in range(n ** 2):
    temp = list(map(int, input().split()))
    students[temp[0]] = temp[1:]

grid = [[0] * n for _ in range(n)]
for s in students.keys():
    i, j = solve(s)
    grid[i][j] = s

total = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < n and 0 <= new_j < n:
                if grid[new_i][new_j] in students[grid[i][j]]:
                    cnt += 1
        if cnt > 0:
            total += 10 ** (cnt - 1)
print(total)