def init():
    n, k = map(int, input().split())
    belt = list(map(int, input().split()))
    return n, k, belt

n, k, belt = init() # 올리는 위치 : 0, 내리는 위치 : n - 1
robot = [0] * n

step = 1
cnt = 0
while True:
    # 1번 과정
    belt = [belt[-1]] + belt[:-1]
    robot = [robot[-1]] + robot[:-1]
    if robot[-1] == 1:
        robot[-1] = 0
    # 2번 과정
    for i in range(n - 2, -1, -1):
        new_i = i + 1
        if robot[i] == 1 and robot[new_i] == 0 and belt[new_i] >= 1:
            robot[new_i] = 1
            robot[i] = 0
            belt[new_i] -= 1
            if belt[new_i] == 0:
                cnt += 1
    if robot[-1] == 1:
        robot[-1] = 0
    # 3번 과정
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1
    # 4번 과정
    if cnt >= k:
        break    
    step += 1

print(step)