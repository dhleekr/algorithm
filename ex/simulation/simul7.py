def init():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m , grid

def calc_distance(houses, chicken):
    total = 0
    for i, j in houses:
        d = 999999999
        for ci, cj in chicken:
            d = min(d, abs(i-ci)+abs(j-cj))
        total += d

    return total

def combination(chicken, m):
    for i in range(len(chicken)):
        if m == 1:
            yield [chicken[i]]
        else:
            for next in combination(chicken[i+1:], m-1):
                yield [chicken[i]] + next

n, m, grid = init()

houses = []
chicken = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            houses.append([i, j])
        elif grid[i][j] == 2:
            chicken.append([i, j])

answer = 999999999
for select in combination(chicken, m):
    answer = min(calc_distance(houses, select), answer)

print(answer)