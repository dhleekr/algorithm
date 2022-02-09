dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def init():
    n = int(input())
    curves = [list(map(int, input().split())) for _ in range(n)]
    return n, curves

def dragon_curve(x, y, d, g):
    res = [[x, y]]
    for i in range(g+1):
        if i == 0:
            res.append([x + dx[d], y + dy[d]])
        else:
            temp = []
            for a, b in res[-2::-1]:
                x, y = res[-1]
                if 0 <= x + y -b <= 100 and 0 <= y -x + a <= 100:
                    temp.append([x + y - b, y - x + a])
            if temp:
                res.extend(temp)
    return res


n, curvees = init() # curves : x, y, d(direction), g(generation)

grid = [[0] * 101 for _ in range(101)]
for x, y, d, g in curvees:
    res = dragon_curve(x, y, d, g)
    for i in res:
        if grid[i[0]][i[1]] == 0:
            grid[i[0]][i[1]] = 1

ans = 0
for i in range(100): # i + 1 까지 하니까 100
    for j in range(100): # j + 1 까지 하니까 100
        if grid[i][j] == 1 and grid[i + 1][j] == 1 and grid[i][j + 1] == 1 and grid[i + 1][j + 1] == 1:
            ans += 1
print(ans)