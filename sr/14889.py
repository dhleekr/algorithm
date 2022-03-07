def init():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, grid

def combination(arr, r):
    if r == 0:
        yield []
    else:
        for i in range(len(arr)):
            if r == 1:
                yield [arr[i]]
            else:
                for j in combination(arr[i + 1:], r - 1):
                    yield [arr[i]] + j


n, grid = init()
ans = 1e10
arr = [i for i in range(n)]

for start in combination(arr, n // 2):
    link = [i for i in range(n) if i not in start]
    start_temp = 0
    link_temp = 0
    for i in start:
        for j in start:
            start_temp += grid[i][j]
    for i in link:
        for j in link:
            link_temp += grid[i][j]
    ans = min(ans, abs(start_temp - link_temp))
print(ans)