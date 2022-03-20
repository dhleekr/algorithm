di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

class shark:
    def __init__(self, s, d, z):
        self.s = s
        self.d = d
        self.z = z

    def __repr__(self):
        return f"[{self.s}, {self.d}, {self.z}]"

def init():
    r, c, m = map(int, input().split())
    grid = [[0] * c for _ in range(r)]
    for _ in range(m):
        i, j, s, d, z = map(int, input().split())
        temp = shark(s, d - 1, z)
        grid[i- 1][j - 1] = temp
    return r, c, m, grid

def catch(j):
    size = 0
    for i in range(r):
        if grid[i][j]:
            size += grid[i][j].z
            grid[i][j] = 0
            break
    return size

def shark_move():
    new = [[0] * c for _ in range(r)]
    shark_idx = []
    for i in range(r):
        for j in range(c):
            if grid[i][j]:
                shark_idx.append([i, j])
    while shark_idx:
        i, j = shark_idx.pop()
        temp = grid[i][j]
        move = grid[i][j].s
        d = grid[i][j].d
        if d < 2:
            move %= (r * 2) - 2
        else:
            move %= (c * 2) - 2
        while move:
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < r and 0 <= new_j < c:
                i = new_i
                j = new_j
            else:
                i -= di[d]
                j -= dj[d]
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                elif d == 3:
                    d = 2
            move -= 1

        temp.d = d
        if new[i][j]:
            if new[i][j].z < temp.z:
                new[i][j] = temp
        else:
            new[i][j] = temp
    return new

r, c, m, grid = init()
ans = 0
for j in range(c):
    ans += catch(j)
    grid = shark_move()

print(ans)