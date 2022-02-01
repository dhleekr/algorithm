n = int(input())
store = list(map(int, input().split()))

dp = [0] * 100

dp[0] = store[0]
dp[1] = max(store[0], store[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + store[i])

print(dp[n-1])