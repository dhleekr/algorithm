di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, m = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(n)]
    return n, m, grid

def find_idx():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'R':
                ri, rj = i, j
            elif grid[i][j] == 'B':
                bi, bj = i, j
    return [ri, rj, bi, bj]

def tilt(i, j, d):
    cnt = 0
    while grid[i + di[d]][j + dj[d]] != '#' and grid[i][j] != 'O':
        i += di[d]
        j += dj[d]
        cnt += 1
    return i, j, cnt
        
def bfs():
    ri, rj, bi, bj = find_idx()
    visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[ri][rj][bi][bj] = 1
    q = [[ri, rj, bi, bj, 1]]
    while q:
        ri, rj, bi, bj, depth = q.pop(0)
        if depth > 10:
            break
        for d in range(4):
            new_ri, new_rj, red_move = tilt(ri, rj, d)
            new_bi, new_bj, blue_move = tilt(bi, bj, d)
            if grid[new_bi][new_bj] != 'O':
                if grid[new_ri][new_rj] == 'O':
                    return depth
                if new_ri == new_bi and new_rj == new_bj:
                    if red_move > blue_move:
                        new_ri -= di[d]
                        new_rj -= dj[d]
                    elif red_move < blue_move:
                        new_bi -= di[d]
                        new_bj -= dj[d]
                if visited[new_ri][new_rj][new_bi][new_bj] == 0:
                    q.append([new_ri, new_rj, new_bi, new_bj, depth + 1])
                    visited[new_ri][new_rj][new_bi][new_bj] = 1
    return -1


if __name__ == "__main__":
    n, m, grid = init()
    print(bfs())