def init():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, grid

def split(x, y, d1, d2):
    visited = [[0] * n for _ in range(n)]
    one = 0
    for i in range(x):
        for j in range(y + 1):
            one += grid[i][j]
            visited[i][j] = 1
    for idx, i in enumerate(range(x, x + d1)):
        for j in range(y - idx):
            one += grid[i][j]
            visited[i][j] = 1

    two = 0
    for i in range(x + 1):
        for j in range(y + 1, n):
            two += grid[i][j]
            visited[i][j] = 1
    for idx, i in enumerate(range(x + 1, x + d2 + 1)):
        for j in range(y + 2 + idx, n):
            two += grid[i][j]
            visited[i][j] = 1

    three = 0
    for idx, i in enumerate(range(x + d1, x + d1 + d2)):
        for j in range(y - d1 + idx):
            three += grid[i][j]
            visited[i][j] = 1
    for i in range(x + d1 + d2, n):
        for j in range(y - d1 + d2):
            three += grid[i][j]
            visited[i][j] = 1

    four = 0
    for idx, i in enumerate(range(x + d2 + 1, x + d1 + d2 + 1)):
        for j in range(y + d2 - idx, n):
            four += grid[i][j]
            visited[i][j] = 1
    for i in range(x + d1 + d2 + 1, n):
        for j in range(y - d1 + d2, n):
            four += grid[i][j]
            visited[i][j] = 1

    five = 0
    res = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                five += grid[i][j]
                res.append([i, j])
    temp = [one, two, three, four, five]
    return max(temp) - min(temp)


n, grid = init()
ans = 1e10
for x in range(n):
    for y in range(n):
        for d1 in range(1, n - 1):
            for d2 in range(1, n - 1):
                if d1 + d2 < n and 0 <= y - d1 < y and y + d2 < n and x + d1 + d2 < n:
                    ans = min(split(x, y, d1, d2), ans)
print(ans)

# def init():
#     n = int(input())
#     grid = [list(map(int, input().split())) for _ in range(n)]
#     return n, grid

# def calc(x, y, d1, d2):
#     first = 0
#     second = 0
#     third = 0
#     fourth = 0
    
#     edge = [[0]*n for _ in range(n)]

#     for i in range(d1+1):
#         edge[x+i][y-i] = 5
#         edge[x+d2+i][y+d2-i] = 5
    
#     for i in range(d2+1):
#         edge[x+i][y+i] = 5
#         edge[x+d1+i][y-d1+i] = 5

#     for i in range(x+d1):
#         for j in range(y+1):
#             if edge[i][j] == 5:
#                 break
#             first += grid[i][j]
        
#     for i in range(x+d2+1):
#         for j in reversed(range(y+1, n)):
#             if edge[i][j] == 5:
#                 break
#             second += grid[i][j]
    
#     for i in range(x+d1, n):
#         for j in range(y-d1+d2):
#             if edge[i][j] == 5:
#                 break
#             third += grid[i][j]
    
#     for i in range(x+d2+1, n):
#         for j in reversed(range(y-d1+d2, n)):
#             if edge[i][j] == 5:
#                 break
#             fourth += grid[i][j]
    
#     fifth = sum(sum(row) for row in grid) - (first + second + third + fourth)

#     return max(first, second, third, fourth, fifth) - min(first, second, third, fourth, fifth)

# n, grid = init()

# min_val = 1e9
# for x in range(n - 1):
#     for y in range(n):
#         for d1 in range(1, y):
#             for d2 in range(1, n - y):
#                 if x + d1 + d2 < n - 1 and 0 <= y - d1 < y and y + d2 < n:
#                     min_val = min(min_val, calc(x, y, d1, d2))

# print(min_val)