def init():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, grid

def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for a in combination(array[i+1:], r - 1):
                yield [array[i]] + a

n, grid = init()
array = [i for i in range(n)]
half = n // 2

min_val = 1e10
for link in combination(array, half):
    start = [i for i in range(n) if i not in link]

    sum_start = 0
    sum_link = 0

    for i in start:
        for j in start:
            if i != j:
                sum_start += grid[i][j]

    for i in link:
        for j in link:
            if i != j:
                sum_link += grid[i][j]

    min_val = min(min_val, abs(sum_start - sum_link))


print(min_val)