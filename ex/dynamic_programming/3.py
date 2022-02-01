n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)
dp =[0] * (n + 2)
max_val = 0

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1):
    temp = i + t[i]
    dp[i] = dp[i + 1] if temp > n + 1 else max(dp[i + 1], dp[temp] + p[i])

print(dp[1])