def init():
    gears = [list(map(int, input().rstrip())) for _ in range(4)]
    k = int(input())
    info = []
    for _ in range(k):
        num, d = map(int, input().split())
        info.append([num - 1, d])
    return gears, k, info

def rotation():
    for num, d in info:
        r_info = [0] * 4
        r_info[num] = d
        for n in range(num , 3):
            if gears[n][2] != gears[n + 1][6]:
                r_info[n + 1] = -r_info[n]
            else:
                break
        for n in range(num, 0, -1):
            if gears[n][6] != gears[n - 1][2]:
                r_info[n - 1] = -r_info[n]
            else:
                break
        for i in range(len(r_info)):
            if r_info[i] == 1:
                gears[i] = [gears[i][-1]] + gears[i][:-1]
            elif r_info[i] == -1:
                gears[i] = gears[i][1:] + [gears[i][0]]

def score():
    ans = 0
    for i in range(4):
        if gears[i][0] == 1:
            ans += 2 ** i
    return ans

gears, k, info = init()
rotation()
print(score())