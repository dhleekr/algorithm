def init():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, grid

def calc(x, y, d1, d2):
    first = 0
    second = 0
    third = 0
    fourth = 0
    
    edge = [[0]*n for _ in range(n)]

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
        for j in range(n-1 , y, -1):
            if edge[i][j] == 5:
                break
            second += grid[i][j]
    
    for i in range(x+d1, n):
        for j in range(y-d1+d2):
            if edge[i][j] == 5:
                break
            third += grid[i][j]
    
    for i in range(x+d2+1, n):
        for j in range(n - 1, y - d1 + d2 - 1, -1):
            if edge[i][j] == 5:
                break
            fourth += grid[i][j]
    
    fifth = sum(sum(row) for row in grid) - (first + second + third + fourth) # 이게 핵심

    return max(first, second, third, fourth, fifth) - min(first, second, third, fourth, fifth)

n, grid = init()

min_val = 1e9
for x in range(n - 1):
    for y in range(n):
        for d1 in range(1, y):
            for d2 in range(1, n - y):
                if x + d1 + d2 < n - 1 and 0 <= y - d1 < y and y + d2 < n:
                    min_val = min(min_val, calc(x, y, d1, d2))

print(min_val)