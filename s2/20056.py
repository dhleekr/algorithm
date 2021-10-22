def init():
    N, M, K = map(int, input().split())

    fireball_list = [list(map(int, input().split())) for _ in range(M)]

    return N, M, K, fireball_list


N, M, K, fireball_list = init()
grid = [[[] for _ in range(N)] for _ in range(N)]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    while fireball_list:
        r, c, m, s, d = fireball_list.pop(0)
        r -= 1
        c -= 1
        new_r = (r + s * dr[d]) % N
        new_c = (c + s * dc[d]) % N
        grid[new_r][new_c].append([m, s, d])

    for r in range(N):
        for c in range(N):
            if len(grid[r][c]) > 1:
                sum_m, sum_s, odd_cnt, even_cnt, cnt = 0, 0, 0, 0, len(grid[r][c])

                while grid[r][c]:
                    m, s, d = grid[r][c].pop(0)
                    sum_m += m
                    sum_s += s

                    if d % 2 == 0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1

                if odd_cnt == cnt or even_cnt == cnt:
                    direction = [0, 2, 4, 6]
                else:
                    direction = [1, 3, 5, 7]

                if sum_m // 5:
                    for d in direction:
                        fireball_list.append([r, c, sum_m // 5, sum_s // cnt, d])

            if len(grid[r][c]) == 1:
                fireball_list.append([r, c] + grid[r][c].pop(0))

print(sum(ball[2] for ball in fireball_list))