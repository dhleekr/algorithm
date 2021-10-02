def init():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    pieces = [list(map(int, input().split())) for _ in range(M)]

    return N, M, board, pieces

def find_idx(a):
    for i in range(N):
        for j in range(N):
            for k in range(len(chess[i][j])):
                if chess[i][j][k][0] == a:
                    return [i, j, k]

def move():
    for num in range(M):
        idx = find_idx(num+1)
        i, j, k = idx
        d = chess[i][j][k][1]

        new_i = i + di[d]
        new_j = j + dj[d]

        if not(0 <= new_i < N and 0 <= new_j < N):
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
        elif board[new_i][new_j] == 2:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2

        chess[i][j][k][1] = d
        new_i = i + di[d]
        new_j = j + dj[d]

        # 흰
        if 0 <= new_i < N and 0 <= new_j < N and board[new_i][new_j] == 0:
            length = len(chess[i][j][k:])
            for _ in range(length):
                chess[new_i][new_j].append(chess[i][j].pop(k))
        # 빨
        elif 0 <= new_i < N and 0 <= new_j < N and board[new_i][new_j] == 1:
            length = len(chess[i][j][k:])
            for _ in range(length):
                chess[new_i][new_j].append(chess[i][j].pop())
        
        if num_check():
            return False
    
    return True
            
def num_check():
    for i in range(N):
        for j in range(N):
            if len(chess[i][j]) >= 4:
                return True          


N, M, board, pieces = init()
chess = [[[] for _ in range(N)] for _ in range(N)]

for idx, piece in enumerate(pieces):
    i, j, d  = piece
    chess[i-1][j-1].append([idx+1, d-1])

# 0 : white, 1 : red, 2 : blue
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

for i in range(1000):
    work = move()
    if not work:
        break
if i < 999:
    print(i+1)
else:
    print(-1)