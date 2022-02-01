t = int(input())

answer = []
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    grid = []
    dp = [[0]*m for _ in range(n)]


    for i in range(0, n*m, m):
        grid.append(array[i:i+m])

    for i in range(n):
        dp[i][0] = grid[i][0]
    
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]) + grid[i][j]
            elif i == n-1:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + grid[i][j]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1], dp[i+1][j-1]) + grid[i][j]

    res = 0
    for i in range(n):
        res = max(res, dp[i][-1])
    answer.append(res)

for res in answer:
    print(res)

print(grid)
print(dp)