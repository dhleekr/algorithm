def init():
    n, l = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, l, grid


n, l, grid = init()

ans = 0
for i in range(n):
    pre = grid[i][0]
    cnt = 1
    for j in range(1,n):
        if grid[i][j] == pre:
            cnt += 1
            pre = grid[i][j]
        elif grid[i][j] == pre + 1 and cnt >= 0:
            if cnt >= l:
                cnt = 1
                pre = grid[i][j]
            else:
                break
        elif grid[i][j] == pre - 1 and cnt >= 0:
            cnt = - l + 1
            pre = grid[i][j]
        else:
            break
    else:
        if cnt >= 0:
            ans += 1
 
for j in range(n):
    pre = grid[0][j]
    cnt = 1
    for i in range(1,n):
        if grid[i][j] == pre:
            cnt += 1
            pre = grid[i][j]
        elif grid[i][j] == pre + 1 and cnt >= 0:
            if cnt >= l:
                cnt = 1
                pre = grid[i][j]
            else:
                break
        elif grid[i][j] == pre - 1 and cnt >= 0:
            cnt = - l + 1
            pre = grid[i][j]
        else:
            break
    else:
        if cnt >= 0:
            ans += 1
 
print(ans)