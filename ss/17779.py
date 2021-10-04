def init():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    return N, grid

def boundary(x, y, d1, d2):
    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0
    visited = []

    for i in range(x+d1):
        for j in range(y+1):
            if i < x:
                first += grid[i][j]
                visited.append([i, j])
            else:
                if j < y-(i-x):
                    first += grid[i][j]
                    visited.append([i, j])
     
    for i in range(x+d2+1):
        for j in range(y+1, N):
            if i <= x:
                second += grid[i][j]
                visited.append([i, j])
            else:
                if j >= y+1+(i-x):
                    second += grid[i][j]
                    visited.append([i, j])

    for i in reversed(range(x+d1, N)):
        for j in range(y-d1+d2):
            if i >= x+d1+d2:
                third += grid[i][j]
                visited.append([i, j])
            else:
                if j < y-d1+d2-((x+d1+d2) - i):
                    third += grid[i][j]
                    visited.append([i, j])
      
    for i in reversed(range(x+d2+1, N)):
        for j in range(y-d1+d2, N):
            if i > x+d1+d2:
                fourth += grid[i][j]
                visited.append([i, j])
            else:
                if j >= y-d1+d2+((x+d1+d2+1) - i):
                    fourth += grid[i][j]
                    visited.append([i, j])

    for i in range(N):
        for j in range(N):
            if [i, j] not in visited:
                fifth += grid[i][j]

    return first, second, third, fourth, fifth

N, grid = init()

ans = 2000
for x in range(N-1):
    for y in range(N):
        for d1 in range(1, y):
            for d2 in range(1, N-y):
                if x+d1+d2 < N-1 and 0 <= y-d1 < y and y+d2 < N:
                    first, second, third, fourth, fifth = boundary(x, y, d1, d2)
                    ans = min(ans, max(first, second, third, fourth, fifth)-min(first, second, third, fourth, fifth))

print(ans)