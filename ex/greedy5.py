n, m = map(int, input().split())
data = list(map(int, input().split()))

weights = [0]*m

for weight in data:
    weights[weight-1] += 1

result = 0

for i in range(m):
    n -= weights[i]
    result += weights[i]*n

print(result)