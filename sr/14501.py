def init():
    n = int(input())
    tps = [list(map(int, input().split())) for _ in range(n)]
    return n, tps

def dfs(t, total):
    global ans
    if t >= n:
        ans = max(ans, total)
        return

    temp_t, temp_p = tps[t]
    if t + temp_t <= n:
        dfs(t + temp_t, total + temp_p)
    dfs(t + 1, total)

n, tps = init()
ans = 0
dfs(0, 0)
print(ans)