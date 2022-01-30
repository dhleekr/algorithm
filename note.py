# 그리드 시계 방향 90도 회전시키는 함수
def rotation(grid):
    m = len(grid)
    new_grid = [[0]*m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            new_grid[j][m-i-1] = grid[i][j]
    
    return new_grid

# Permutation 함수 구현
def permutation(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutation(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next

# Combination 함수 구현
def combination(array, m):
    for i in range(len(array)):
        if m == 1:
            yield [array[i]]
        else:
            for next in combination(array[i+1:], m-1):
                yield [array[i]] + next

# Deepcopy 구현
def deepcopy(grid):
    new_grid = []
    for i in range(N):
        new_grid.append(grid[i][:])
    return new_grid

# Graph 표현
graph = [[] for _ in range(n+1)] # n : node 개수
for _ in range(e): # e : edge 개수
    graph[a].append(b) # a -> b
