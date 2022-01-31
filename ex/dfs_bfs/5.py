def init():
    n = int(input())
    numbers = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    return n, numbers, add, sub, mul, div

def dfs(i, now):
    global min_num, max_num, add, sub, mul, div

    if i == n:
        min_num = min(min_num, now)
        max_num = max(max_num, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - numbers[i])
            sub += 1
        if mul > 0:
            mul -=1
            dfs(i+1, now * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/numbers[i]))
            div += 1
            
n, numbers, add, sub, mul, div = init()
max_num = -10000000000
min_num = 1000000000
dfs(1, numbers[0])
print(max_num)
print(min_num)