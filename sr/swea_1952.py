def init():
    fees = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    return fees, plan

def dfs(total, month):
    global ans
    if month > 11:
        ans = min(ans, total)
        return
    if plan[month] * fees[0] < fees[1]:
        dfs(total + plan[month] * fees[0], month + 1)
    else:
        dfs(total + fees[1], month + 1)
    if plan[month]:
        dfs(total + fees[2], month + 3)


T = int(input())
for idx in range(1, T + 1):
    fees, plan = init()
    ans = fees[-1]
    dfs(0, 0)
    print(f'#{idx} {ans}')