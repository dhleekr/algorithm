def check(n, m, grid):
    for i in range(m, n + m):
        for j in range(m, n + m):
            if grid[i][j] == 0:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    grid = [[0] * (n + 2*m) for _ in range(n + 2*m)]
    for i in range(n):
        for j in range(n):
            grid[m + i][m + j] = lock[i][j]
    for _ in range(4):
        for i in range(n + m):
            for j in range(n + m):
                visited = []
                flag = True
                for a in range(m):
                    for b in range(m):
                        if key[a][b] == 1:
                            if grid[i + a][j + b] == 0:
                                grid[i + a][j + b] = key[a][b]
                                visited.append([i + a, j + b])
                            else:
                                flag = False
                                break
                    if not flag:
                        break
                        
                if check(n, m, grid):
                    return True
                for vi, vj in visited:
                    grid[vi][vj] = 0
        grid = [list(row) for row in zip(*grid[::-1])]
    return False