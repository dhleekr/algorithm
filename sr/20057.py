di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

def init():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, grid

def tornado_idx():
    idx = []
    i, j = n // 2, n // 2
    cnt = 0
    check = 0
    s, d = 0, 0
    while cnt < n ** 2 - 1:
        if check % 2 == 0:
            s += 1
        for _ in range(s):
            i += di[d]
            j += dj[d]
            cnt += 1
            if cnt == n ** 2:
                break
            idx.append([i, j, d])
        check += 1
        d = (d + 1) % 4
    return idx

def solve():
    global ans
    for i, j, d in tornado_idx():
        total = 0
        new_i = i + 2 * di[d]
        new_j = j + 2 * dj[d]
        if not (0 <= new_i < n and 0 <= new_j < n):
            ans += int(grid[i][j] * 0.05)
        else:
            grid[new_i][new_j] += int(grid[i][j] * 0.05)
        total += int(grid[i][j] * 0.05)

        new_i = i + di[d] + di[(d - 1) % 4]
        new_j = j + dj[d] + dj[(d - 1) % 4]
        if not (0 <= new_i < n and 0 <= new_j < n):
            ans += int(grid[i][j] * 0.1)
        else:
            grid[new_i][new_j] += int(grid[i][j] * 0.1)
        total += int(grid[i][j] * 0.1)

        new_i = i + di[(d - 1) % 4]
        new_j = j + dj[(d - 1) % 4]
        if not (0 <= new_i < n and 0 <= new_j < n):
            ans += int(grid[i][j] * 0.07)
        else:
            grid[new_i][new_j] += int(grid[i][j] * 0.07)
        total += int(grid[i][j] * 0.07)

        new_i = i + 2 * di[(d - 1) % 4]
        new_j = j + 2 * dj[(d - 1) % 4]
        if not (0 <= new_i < n and 0 <= new_j < n):
            ans += int(grid[i][j] * 0.02)
        else:
            grid[new_i][new_j] += int(grid[i][j] * 0.02)
        total += int(grid[i][j] * 0.02)

        new_i = i - di[d] + di[(d - 1) % 4]
        new_j = j - dj[d] + dj[(d - 1) % 4]
        if not (0 <= new_i < n and 0 <= new_j < n):
            ans += int(grid[i][j] * 0.01)
        else:
            grid[new_i][new_j] += int(grid[i][j] * 0.01)
        total += int(grid[i][j] * 0.01)

        new_i = i + di[d] + di[(d + 1) % 4]
        new_j = j + dj[d] + dj[(d + 1) % 4]
        if not (0 <= new_i < n and 0 <= new_j < n):
            ans += int(grid[i][j] * 0.1)
        else:
            grid[new_i][new_j] += int(grid[i][j] * 0.1)
        total += int(grid[i][j] * 0.1)

        new_i = i + di[(d + 1) % 4]
        new_j = j + dj[(d + 1) % 4]
        if not (0 <= new_i < n and 0 <= new_j < n):
            ans += int(grid[i][j] * 0.07)
        else:
            grid[new_i][new_j] += int(grid[i][j] * 0.07)
        total += int(grid[i][j] * 0.07)

        new_i = i + 2 * di[(d + 1) % 4]
        new_j = j + 2 * dj[(d + 1) % 4]
        if not (0 <= new_i < n and 0 <= new_j < n):
            ans += int(grid[i][j] * 0.02)
        else:
            grid[new_i][new_j] += int(grid[i][j] * 0.02)
        total += int(grid[i][j] * 0.02)

        new_i = i - di[d] + di[(d + 1) % 4]
        new_j = j - dj[d] + dj[(d + 1) % 4]
        if not (0 <= new_i < n and 0 <= new_j < n):
            ans += int(grid[i][j] * 0.01)
        else:
            grid[new_i][new_j] += int(grid[i][j] * 0.01)
        total += int(grid[i][j] * 0.01)

        new_i = i + di[d]
        new_j = j + dj[d]
        if not (0 <= new_i < n and 0 <= new_j < n):
            ans += grid[i][j] - total
        else:
            grid[new_i][new_j] += grid[i][j] - total

        grid[i][j] = 0


n, grid = init()
ans = 0
solve()
print(ans)