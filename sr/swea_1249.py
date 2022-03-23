def init():
    n = int(input())
    grid = [list(map(int, input().rstrip())) for _ in range(n)]
    return n, grid

def bfs():
    dist_map = [[1e10] * n for _ in range(n)]
    dist_map[0][0] = 0
    q = [[0, 0]]
    while q:
        i, j = q.pop(0)
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < n and 0 <= new_j < n and dist_map[new_i][new_j] > dist_map[i][j] + grid[new_i][new_j]:
                dist_map[new_i][new_j] = dist_map[i][j] + grid[new_i][new_j]
                q.append([new_i, new_j])
    return dist_map


if __name__ == "__main__":
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    T = int(input())
    ans = []
    for _ in range(T):
        n, grid = init()
        dist_map = bfs()
        min_val = dist_map[n - 1][n - 1]
        ans.append(min_val)

    for idx, v in enumerate(ans):
        print(f"#{idx + 1} {v}")