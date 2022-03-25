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
    
def calc_dist(chick):
    total = 0
    for i, j in houses:
        min_dist = 1e10
        for ci, cj in chick:
            min_dist = min((abs(i - ci) + abs(j - cj)), min_dist)
        total += min_dist
    return total

def dfs(cur, arr):
    global min_total

    if len(arr) == m:
        min_total = min(min_total, calc_dist(arr))
        return
    if cur == len(chickens):
        return
    dfs(cur + 1, arr + [chickens[cur]])
    dfs(cur + 1, arr)


n, m, grid = init()
houses, chickens = find_idx()
min_total = 1e10
dfs(0, [])
print(min_total)