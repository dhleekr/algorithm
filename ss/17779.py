def init():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    return N, grid

def boundary(x, y, d1, d2):
    first = 0
    second = 0
    third = 0
    fourth = 0
    
    edge = [[0]*N for _ in range(N)]

    for i in range(d1+1):
        edge[x+i][y-i] = 5
        edge[x+d2+i][y+d2-i] = 5
    
    for i in range(d2+1):
        edge[x+i][y+i] = 5
        edge[x+d1+i][y-d1+i] = 5

    for i in range(x+d1):
        for j in range(y+1):
            if edge[i][j] == 5:
                break
            first += grid[i][j]
        
    for i in range(x+d2+1):
        for j in reversed(range(y+1, N)):
            if edge[i][j] == 5:
                break
            second += grid[i][j]
    
    for i in range(x+d1, N):
        for j in range(y-d1+d2):
            if edge[i][j] == 5:
                break
            third += grid[i][j]
    
    for i in range(x+d2+1, N):
        for j in reversed(range(y-d1+d2, N)):
            if edge[i][j] == 5:
                break
            fourth += grid[i][j]
    
    fifth = sum(sum(row) for row in grid) - (first + second + third + fourth)

    return max(first, second, third, fourth, fifth) - min(first, second, third, fourth, fifth)

N, grid = init()

ans = 2000
for x in range(N-1):
    for y in range(N):
        for d1 in range(1, y):
            for d2 in range(1, N-y):
                if x+d1+d2 < N-1 and 0 <= y-d1 < y and y+d2 < N:
                    ans = min(ans, boundary(x, y, d1, d2))

print(ans)