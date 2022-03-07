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
for temp in combination([1,2,3,4], 1):
    print(temp)