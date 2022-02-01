n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*i for i in range(1, n+1)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    length = len(triangle[i])
    for j in range(length):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == length - 1:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[n-1]))