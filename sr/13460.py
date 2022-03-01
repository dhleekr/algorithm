di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    return n, m, grid

def pos():
    ri, rj, bi, bj = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'R':
                ri, rj = i, j
            elif grid[i][j] == 'B':
                bi, bj = i, j
    q.append((ri, rj, bi, bj, 1))
    visited[ri][rj][bi][bj] = True

def move(i, j, d):
    cnt = 0
    while grid[i + di[d]][j + dj[d]] != '#' and grid[i][j] != 'O':
        i += di[d]
        j += dj[d]
        cnt += 1
    return i, j, cnt

def solve():
    pos()
    while q:
        ri, rj, bi, bj, depth = q.pop(0)
        if depth > 10:
            break
        
        for d in range(4):
            nri, nrj, rcnt = move(ri, rj, d)
            nbi, nbj, bcnt = move(bi, bj, d)
            if grid[nbi][nbj] != 'O':
                if grid[nri][nrj] == 'O':
                    print(depth)
                    return
                if nri == nbi and nrj == nbj:
                    if rcnt > bcnt:
                        nri -= di[d]
                        nrj -= dj[d]
                    else:
                        nbi -= di[d]
                        nbj -= dj[d]
                if not visited[nri][nrj][nbi][nbj]:
                    visited[nri][nrj][nbi][nbj] = True
                    q.append((nri, nrj, nbi, nbj, depth + 1))
    print(-1)


n, m, grid = init()
q = []
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

solve()