def dfs(total, depth, plus, minus, mul, div):
    global min_val, max_val

    if depth == n:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return
    
    if plus:
        dfs(total + numbers[depth], depth + 1, plus - 1, minus, mul, div)
    if minus:
        dfs(total - numbers[depth], depth + 1, plus, minus - 1, mul, div)
    if mul:
        dfs(total * numbers[depth], depth + 1, plus, minus, mul - 1, div)
    if div:
        dfs(int(total / numbers[depth]), depth + 1, plus, minus, mul, div - 1)

n = int(input())
numbers = list(map(int, input().split()))
operation = list(map(int, input().split()))

min_val, max_val = 1e10, -1e10
dfs(numbers[0], 1, operation[0], operation[1], operation[2], operation[3])

print(max_val)
print(min_val)