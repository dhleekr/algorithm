def init():
    N, M, fuel = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    start = list(map(int, input().split()))
    passengers = [list(map(int, input().split())) for _ in range(M)]

    for i in range(2):
        start[i] -= 1
    for i in range(len(passengers)):
        for j in range(4):
            passengers[i][j] -= 1

    return N, M, fuel, grid, start, passengers

def distance_check(start):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    distance = [[-1]*N for _ in range(N)]
    distance[start[0]][start[1]] = 0
    visited = [[0]*N for _ in range(N)]
    queue = [start]
    visited[start[0]][start[1]] = 1

    while queue:
        i, j = queue.pop(0)
        for idx in range(4):
            new_i = i + di[idx]
            new_j = j + dj[idx]

            if 0 <= new_i < N and 0 <= new_j < N and grid[new_i][new_j] != 1 and not visited[new_i][new_j]:
                queue.append([new_i, new_j])
                visited[new_i][new_j] = 1
                distance[new_i][new_j] = distance[i][j] + 1

    return distance

N, M, fuel, grid, start, passengers = init()

distance = distance_check(start)

while passengers:
    order = []
    for passenger in passengers:
        temp = [distance[passenger[0]][passenger[1]]]
        temp.extend(passenger)
        order.append(temp)
    order.sort(key = lambda x:[x[0], x[1], x[2]])

    p = order.pop(0)
    for i in range(len(passengers)):
        if p[1:] == passengers[i]:
            passengers.pop(i)
            break
    
    fuel -= p[0]
    if fuel < 0 or p[0] == -1:
        fuel = -1
        break
    else:
        distance = distance_check(p[1:3])
        d = distance[p[3]][p[4]]
        fuel -= d
        if fuel < 0 or d == -1:
            fuel = -1
            break
        else:
            fuel += 2*d

        distance = distance_check(p[3:5])

print(fuel)