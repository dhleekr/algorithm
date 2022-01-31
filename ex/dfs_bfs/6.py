di = [0, 1, 0, -1]
dj = [1, 0, -1 ,0]

def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for j in combination(array[i+1:], r-1):
                yield [array[i]] + j

def find_idx(grid, num):
    res = []
    length = len(grid)
    for i in range(length):
        for j in range(length):
            if grid[i][j] == num:
                res.append([i, j])
    return res

def monitor(grid, idx, d):
    i, j = idx
    n = len(grid)
    new_i = i + di[d]
    new_j = j + dj[d]

    if 0 <= new_i < n and 0 <= new_j < n:
        if grid[new_i][new_j] == 'S':
            return 1
        elif grid[new_i][new_j] == 'X':
            return monitor(grid, [new_i, new_j], d)
    return 0  

def solution(grid, empty, teachers):
    possible = False
    for obs in combination(empty, 3):
        for i, j in obs:
            grid[i][j] = 'O'
            
        ans = 0
        for teacher in teachers:
            for d in range(4):
                ans += monitor(grid, teacher, d)
        if ans == 0:
            possible = True
            break

        for i, j in obs:
            grid[i][j] = 'X'

    if possible:
        return 'YES'
    else:
        return 'NO'


n = int(input())
grid = [list(input().split()) for _ in range(n)]
teachers = find_idx(grid, 'T')
empty = find_idx(grid, 'X')
print(solution(grid, empty, teachers))