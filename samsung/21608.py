def init(): # input
    N = int(input())

    students = []
    for _ in range(N**2):
        temp = list(map(int, input().split()))
        students.append(temp)

    return N, students

def adjacent_check(N, grid, position, favorite): # 비어있는 칸의 position과 favorite 받아서 그 칸의 인접한 favorite 수 반환
    num_favorite = 0
    num_empty = 0
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for idx in range(4):
        i = position[0] + di[idx]
        j = position[1] + dj[idx]

        if 0 <= i < N and 0 <= j < N:
            if grid[i][j] in favorite:
                num_favorite += 1
            
            if grid[i][j] == 0:
                num_empty += 1
    
    return num_favorite, num_empty

def favorite_check(N, grid, favorite):
    empty = []
    # 비어있는 칸
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                empty.append((i, j))

    candidate = []
    for i, j in empty:
        num_favorite, num_empty = adjacent_check(N, grid, (i, j), favorite)
        temp = [num_favorite, num_empty]
        temp.append((i, j))
        candidate.append(temp)
    
    candidate.sort(reverse=True)
    return candidate[0]

def satisfy(N, grid, student, favorite):
    ans = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == student:
                idx = (i, j)
    
    num_favorite, num_empty = adjacent_check(N, grid, idx, favorite)
    if num_favorite == 1:
        ans += 1
    elif num_favorite == 2:
        ans += 10
    elif num_favorite == 3:
        ans += 100
    elif num_favorite == 4:
        ans += 1000
    
    return ans


N, students = init() # students -> [0] : 해당학생, [1:] : favorite
grid = [[0]*N for _ in range(N)]

for i in range(N**2):
    a = favorite_check(N, grid, students[i][1:])
    grid[a[2][0]][a[2][1]] = students[i][0]
ans = 0
for i in range(N**2):
    
    temp = satisfy(N, grid, students[i][0], students[i][1:])
    ans += temp

print(ans)