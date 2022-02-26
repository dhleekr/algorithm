def init():
    n, m, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    xdk = [list(map(int, input().split())) for _ in range(t)]
    return n, m, t, board, xdk

def rotation(arr, d, k):
    new = arr[:]
    if d == 0: # 시계방향
        for i in range(m):
            new[(i + k) % m] = arr[i]
    elif d == 1: # 반시계방향
        for i in range(m):
            new[(i - k) % m] = arr[i]
    return new

def check():
    neighbors = []
    for i in range(n):
        for j in range(m):
            if board[i][j] != 'x':
                if j == m - 1:
                    if board[i][j] == board[i][0]:
                        neighbors.append([i, j])
                        neighbors.append([i, 0])
                else:
                    if board[i][j] == board[i][j + 1]:
                        neighbors.append([i, j])
                        neighbors.append([i, j + 1])
    
    for j in range(m):
        for i in range(n - 1):
            if board[i][j] != 'x':
                if i == n - 1:
                    if board[i][j] == board[0][j]:
                        neighbors.append([i, j])
                        neighbors.append([0, j])
                else:
                    if board[i][j] == board[i + 1][j]:
                        neighbors.append([i, j])
                        neighbors.append([i + 1, j])
    
    if neighbors:
        for i, j in neighbors:
            board[i][j] = 'x'
    else:
        total = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] != 'x':
                    total += board[i][j]
                    cnt += 1
        if cnt:
            avg = total / cnt
        for i in range(n):
            for j in range(m):
                if board[i][j] != 'x':
                    if board[i][j] > avg:
                        board[i][j] -= 1
                    elif board[i][j] < avg:
                        board[i][j] += 1

n, m, t, board, xdk = init()
for a in range(t):
    x, d, k = xdk[a]
    for i in range(x - 1, n, x):
        board[i] = rotation(board[i], d, k)
    check()

total = 0
for i in range(n):
    for j in range(m):
        if board[i][j] != 'x':
            total += board[i][j]
print(total)