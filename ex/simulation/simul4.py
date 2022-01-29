def rotation(grid):
    m = len(grid)
    new_grid = [[0]*m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            new_grid[j][m-i-1] = grid[i][j]
    
    return new_grid

def check(lock):
    length = len(lock)//3
    for i in range(length, length*2):
        for j in range(length, length*2):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*3*n for _ in range(3*n)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    for _ in range(4):
        key = rotation(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
            
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))