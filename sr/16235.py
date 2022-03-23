di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

def init():
    n, m, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    tree = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        tree[x - 1][y - 1].append(z)
    return n, m, k, A, tree

def spring_summer():
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                temp_tree, dead = [], 0
                for t in tree[i][j]:
                    if t <= grid[i][j]:
                        grid[i][j] -= t
                        t += 1
                        temp_tree.append(t)
                    else:
                        dead += t // 2
                grid[i][j] += dead
                tree[i][j] = []
                tree[i][j].extend(temp_tree)

def fall():
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for t in tree[i][j]:
                    if t % 5 == 0:
                        for d in range(8):
                            new_i = i + di[d]
                            new_j = j + dj[d]
                            if 0 <= new_i < n and 0 <= new_j < n:
                                tree[new_i][new_j].append(1)

def winter():
    for i in range(n):
        for j in range(n):
            grid[i][j] += A[i][j]

def cnt():
    ans = 0
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                ans += len(tree[i][j])
    return ans



if __name__ == "__main__":
    n, m, k, A, tree = init()
    grid = [[5] * n for _ in range(n)]
    for _ in range(k):
        spring_summer()
        fall()
        winter()
    print(cnt())