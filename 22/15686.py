def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, grid

def find_idx(num):
    res = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                res.append([i, j])
    return res

def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for a in combination(arr[i+1:], r - 1):
                yield [arr[i]] + a

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(case, houses):
    res = 0
    for h in houses:
        temp = 1e10
        for c in case:
            temp = min(temp, dist(c, h))
        res += temp
    return res

n, m, grid = init()
houses = find_idx(1)
chickens = find_idx(2)

min_dist = 1e10
for case in combination(chickens, m):
    min_dist = min(min_dist, solution(case, houses))
print(min_dist)