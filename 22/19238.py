di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def init():
    n, m, fuel = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range (n)]
    start = list(map(lambda x: int(x) - 1, input().split()))
    passengers = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]    
    return n, m, fuel, grid,start, passengers

def calc_dist(start):
    distance = [[-1] * n for _ in range(n)]
    distance[start[0]][start[1]] = 0
    visited = [[0] * n for _ in range(n)]
    visited[start[0]][start[1]] = 1
    q = [start]
    while q:
        i, j = q.pop(0)
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] != 1 and visited[new_i][new_j] == 0:
                q.append([new_i, new_j])
                visited[new_i][new_j] = 1
                distance[new_i][new_j] = distance[i][j] + 1

    return distance


n, m, fuel, grid, start, passengers = init()
distance = calc_dist(start)
while passengers:
    order = []
    for passenger in passengers:
        dist = distance[passenger[0]][passenger[1]]
        order.append([dist] + passenger)
    order.sort(key=lambda x : (x[0], x[1], x[2]))

    p = order.pop(0)
    for i in range(m):
        if p[1:] == passengers[i]:
            passengers.pop(i)
            break

    fuel -= p[0]
    if fuel < 0 or p[0] == -1:
        fuel = -1
        break
    else:
        distance = calc_dist(p[1:3])
        dist = distance[p[3]][p[4]]
        fuel -= dist
        if fuel < 0 or dist == -1:
            fuel = -1
            break
        else:
            fuel += 2 * dist
        distance = calc_dist(p[3:5])
        
print(fuel)