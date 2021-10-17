# grid 2차원 배열일 때
def deepcopy(grid):
    new_grid = []
    for i in range(N):
        new_grid.append(grid[i][:])

    return new_grid

def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for n in combination(array[i+1:], r-1):
                yield [array[i]] + n
