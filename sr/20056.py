di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

class fireball:
    def __init__(self, m, s, d):
        self.m = m
        self.s = s
        self.d = d

    def __repr__(self):
        return f"[{self.m}, {self.s}, {self.d}]"
        
def init():
    N, M, k = map(int, input().split())
    grid = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        temp = fireball(m, s, d)
        grid[r - 1][c - 1].append(temp)
    return N, M, k, grid

def move():
    new = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                while grid[i][j]:
                    temp = grid[i][j].pop()
                    new_i = (i + temp.s * di[temp.d]) % N
                    new_j = (j + temp.s * dj[temp.d]) % N
                    new[new_i][new_j].append(temp)
    return new

def add():
    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) > 1:
                sum_m = 0
                sum_s = 0
                is_even = False
                is_odd = False
                cnt = len(grid[i][j])
                while grid[i][j]:
                    temp = grid[i][j].pop()
                    sum_m += temp.m
                    sum_s += temp.s
                    if temp.d % 2 == 0:
                        is_even = True
                    else:
                        is_odd = True
                if is_even and is_odd:
                    d_list = [1, 3, 5, 7]
                else:
                    d_list = [0, 2, 4, 6]
                for k in range(4):
                    if sum_m // 5 > 0:
                        grid[i][j].append(fireball(sum_m // 5, sum_s // cnt, d_list[k]))


N, M, k, grid = init()
for _ in range(k):
    grid = move()
    add()

ans = 0
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            for k in range(len(grid[i][j])):
                ans += grid[i][j][k].m
print(ans)