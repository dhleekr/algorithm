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

def check_square(x, y, arr):
    for d in range(4):
        x += dx[d]
        y += dy[d]
        if [x, y] not in arr:
            return False
    return True


n, curvees = init() # curves : x, y, d(direction), g(generation)
arr = []
for x, y, d, g in curvees:
    res = dragon_curve(x, y, d, g)
    for i in res:
        if i not in arr:
            arr.append(i)

ans = 0
for x, y in arr:
    if check_square(x, y, arr):
        ans += 1
print(ans)