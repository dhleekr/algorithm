def init():
    n = int(input())
    numbers = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    return n, numbers, add, sub, mul, div

def dfs(add, sub, mul, div, total, depth):
    global max_val, min_val
    if depth == n:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return

    num = numbers[depth]

    if add:
        dfs(add - 1, sub, mul, div, total + num, depth + 1)
    if sub:
        dfs(add, sub - 1, mul, div, total - num, depth + 1)
    if mul:
        dfs(add, sub, mul - 1, div, total * num, depth + 1)
    if div:
        if total >= 0:
            dfs(add, sub, mul, div - 1, total // num, depth + 1)
        else:
            dfs(add, sub, mul, div - 1, -(abs(total) // num), depth + 1)


n, numbers, add, sub, mul, div = init()
max_val, min_val = -1e10, 1e10
dfs(add, sub, mul, div, numbers[0], 1)
print(max_val)
print(min_val)