def init():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    return N, grid


def make_order():
    i = N // 2
    j = N // 2
    order = []
    directions = []

    step = 0
    cd = 0
    stop = False

    while True:
        if cd % 2 == 0:
            step += 1

        for _ in range(step):
            i += di[cd]
            j += dj[cd]
            order.append([i, j])
            directions.append(cd)
        
            if i == 0 and j == 0:
                stop = True
                break
        if stop:
            break

        cd = (cd + 1) % 4

    return order, directions


def tornado():
    outside = 0
    weight = [0.05, 0.1, 0.1, 0.07, 0.02, 0.07, 0.02, 0.01, 0.01, 0]
    for idx, (i, j) in enumerate(order):
        d = directions[idx]

        f_1_i, f_1_j = i + di[d], j + dj[d]
        f_2_i, f_2_j = i + 2*di[d], j + 2*dj[d]

        fr_1_i, fr_1_j = i + + di[d] + di[(d+3)%4], j + dj[d] + dj[(d+3)%4]
        fl_1_i, fl_1_j = i + di[d] + di[(d+1)%4], j + dj[d] + dj[(d+1)%4]

        r_1_i, r_1_j = i + di[(d+3)%4], j + dj[(d+3)%4]
        r_2_i, r_2_j = i + 2*di[(d+3)%4], j + 2*dj[(d+3)%4]

        l_1_i, l_1_j = i + di[(d+1)%4], j + dj[(d+1)%4]
        l_2_i, l_2_j = i + 2*di[(d+1)%4], j + 2*dj[(d+1)%4]

        br_1_i, br_1_j = i + di[(d+2)%4] + di[(d+3)%4], j +dj[(d+2)%4] + dj[(d+3)%4]
        bl_1_i, bl_1_j = i + + di[(d+1)%4] + di[(d+2)%4], j + dj[(d+1)%4] + dj[(d+2)%4]
        
        new = [[f_2_i, f_2_j], [fr_1_i, fr_1_j], [fl_1_i, fl_1_j], 
                [r_1_i, r_1_j], [r_2_i, r_2_j], [l_1_i, l_1_j], [l_2_i, l_2_j],
                [br_1_i, br_1_j], [bl_1_i, bl_1_j], [f_1_i, f_1_j]]

        temp = 0
        for idx, (new_i, new_j) in enumerate(new):
            # print(grid, (new_i, new_j))
            temp += int(weight[idx]*grid[i][j])

            if 0 <= new_i < N and 0 <= new_j < N:
                if idx < 9:
                    grid[new_i][new_j] += int(weight[idx]*grid[i][j])
                else:
                    grid[new_i][new_j] += grid[i][j] - temp
            else:
                if idx < 9:
                    outside += (int(weight[idx]*grid[i][j]))
                else:
                    outside += grid[i][j] - temp

            if idx == len(new)-1:
                grid[i][j] = 0

    
    return outside


N, grid = init()

di = [0, 1, 0, -1]  # 좌 하 우 상
dj = [-1, 0, 1, 0]

order, directions = make_order()
outside = tornado()

# print(grid)
print(outside)