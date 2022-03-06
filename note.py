arr = [[]] # 기존 행렬
arr_2 = [list(a) for a in zip(*arr[::-1])] # 시계 방향 90도
arr_3 = [list(a) for a in zip(*arr)][::-1] # 반시계 방향 90도

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

# Combination 함수 yield 안쓰고 구현 (yield로 하면 r이 0일 때, 아무값도 안나오는데 그러면 안되고 [] 이렇게 나와야하는 경우가 있음)
def combinations(arr,r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield [arr[i]]+next

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
