def init():
    n = int(input())
    tp = [list(map(int, input().split())) for _ in range(n)]
    return n, tp

def dfs(day, profit):
    global ans
    if day == n:
        ans = max(ans, profit)
        return
    
    t, p = tp[day]
    if day + t <= n:
        dfs(day + t, profit + p)
    dfs(day + 1, profit)

n, tp = init()
ans = 0
dfs(0, 0)
print(ans)