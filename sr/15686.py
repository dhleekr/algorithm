def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, grid

def find_idx():
    houses = []
    chickens = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                houses.append([i, j])
            elif grid[i][j] == 2:
                chickens.append([i, j])
    return houses, chickens

def combination(arr, r):
    if r == 0:
        return []
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combination(arr[i + 1:], r - 1):
                yield [arr[i]] + j

def calc_dist(chick):
    total = 0
    for i, j in houses:
        min_dist = 1e10
        for ci, cj in chick:
            min_dist = min((abs(i - ci) + abs(j - cj)), min_dist)
        total += min_dist
    return total


n, m, grid = init()
houses, chickens = find_idx()
min_total = 1e10
for chick in combination(chickens, m):
    min_total = min(calc_dist(chick), min_total)
print(min_total)