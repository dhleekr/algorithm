def init():
    N, M, T = map(int, input().split())
    disk = [list(map(int, input().split())) for _ in range(N)]
    spin_info = [list(map(int, input().split())) for _ in range(T)]

    return N, M, T, disk, spin_info

def cw(array, k):
    while k > 0:
        new = [array.pop()]
        new.extend(array)
        k -= 1
        array = new
    return array

def ccw(array, k):
    while k > 0:
        array.append(array.pop(0))
        k -= 1
    return array

def spin(info):
    x, d, k = info
    for i in range(x-1, len(disk), x):
        if d == 0:
            disk[i] = cw(disk[i], k)
        else:
            disk[i] = ccw(disk[i], k)

def adjacent():
    idx = []
    for i in range(N):
        for j in range(M):
            if disk[i][j] == disk[i][(j+1)%M] and disk[i][j] != 0:
                if [i, j] not in idx:
                    idx.append([i, j])
                if [i, (j+1)%M] not in idx:
                    idx.append([i, (j+1)%M])
            if disk[i][j] == disk[i][(j-1)%M] and disk[i][j] != 0:
                if [i, j] not in idx:
                    idx.append([i, j])
                if [i, (j-1)%M] not in idx:
                    idx.append([i, (j-1)%M])

            if i != 0 and i != N-1:
                if disk[i][j] == disk[(i+1)%N][j] and disk[i][j] != 0:
                    if [i, j] not in idx:
                        idx.append([i, j])
                    if [(i+1)%N, j] not in idx:
                        idx.append([(i+1)%N, j])
                if disk[i][j] == disk[(i-1)%N][j] and disk[i][j] != 0:
                    if [i, j] not in idx:
                        idx.append([i, j])
                    if [(i-1)%N, j] not in idx:
                        idx.append([(i-1)%N, j])
            if i == 0:
                if disk[i][j] == disk[(i+1)%N][j] and disk[i][j] != 0:
                    if [i, j] not in idx:
                        idx.append([i, j])
                    if [(i+1)%N, j] not in idx:
                        idx.append([(i+1)%N, j])
            if i == N-1:
                if disk[i][j] == disk[(i-1)%N][j] and disk[i][j] != 0:
                    if [i, j] not in idx:
                        idx.append([i, j])
                    if [(i-1)%N, j] not in idx:
                        idx.append([(i-1)%N, j])

    return idx


N, M, T, disk, spin_info = init()

for info in spin_info:
    if sum(sum(row) for row in disk) == 0:
        break
    spin(info)
    idx = adjacent()
    if idx:
        for a in idx:
            i, j = a
            disk[i][j] = 0
    else:
        total = 0
        cnt = 0
        not_zero_idx = []
        for i in range(N):
            for j in range(M):
                if disk[i][j] != 0:
                    total += disk[i][j]
                    cnt += 1
                    not_zero_idx.append([i, j])
        mean = total / cnt

        for idx in not_zero_idx:
            i, j = idx
            if disk[i][j] > mean:
                disk[i][j] -= 1
            elif disk[i][j] < mean:
                disk[i][j] += 1

print(sum(sum(row) for row in disk))