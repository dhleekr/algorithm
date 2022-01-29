# 그리드 시계 방향 90도 회전시키는 함수
def rotation(grid):
    m = len(grid)
    new_grid = [[0]*m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            new_grid[j][m-i-1] = grid[i][j]
    
    return new_grid


# Combination 함수 구현
def combination(chicken, m):
    for i in range(len(chicken)):
        if m == 1:
            yield [chicken[i]]
        else:
            for next in combination(chicken[i+1:], m-1):
                yield [chicken[i]] + next