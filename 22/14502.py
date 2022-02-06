di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, grid

def find_idx(grid, num):
    res = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == num:
                res.append([i, j])
    return res

def spread(grid, virus_indices):
    visited = [[False] * m for _ in range(n)]
    while virus_indices:
        i, j = virus_indices.pop(0)
        visited[i][j] = True
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 0 and not visited[new_i][new_j]:
                visited[new_i][new_j] = True
                virus_indices.append([new_i, new_j])
                grid[new_i][new_j] = 2
    return len(find_idx(grid, 0))

def combination(array, m):
    for i in range(len(array)):
        if m == 1:
            yield [array[i]]
        else:
            for next in combination(array[i+1:], m-1):
                yield [array[i]] + next

def deepcopy(grid):
    new = []
    for i in range(len(grid)):
        new.append(grid[i][:])
    return new


n, m, original = init()

empty = find_idx(original, 0)

max_area = 0
for walls in combination(empty, 3):
    grid = deepcopy(original)
    virus_indices = find_idx(grid, 2)
    for i, j in walls:
        grid[i][j] = 1
    max_area = max(spread(grid, virus_indices), max_area)

print(max_area)