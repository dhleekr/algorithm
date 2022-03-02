def init():
    n = int(input())
    eq = list(input().rstrip())
    num, op = [], []
    for e in eq:
        num.append(e) if e.isdigit() else op.append(e)
    return n, num, op

def dfs(idx, total):
    global ans
    if idx == len(op):
        ans = max(ans, int(total))
        return

    first = str(eval(total + op[idx] + num[idx + 1]))
    dfs(idx + 1, first)

    if idx + 1 < len(op):
        second = str(eval(num[idx + 1] + op[idx + 1] + num[idx + 2]))
        second = str(eval(total + op[idx] + second))
        dfs(idx + 2, second)


n, num, op = init()
ans = -(2**31)
dfs(0, num[0])
print(ans)