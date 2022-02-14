def init():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

def belt_rotate(a):
    for i in range(len(robot) - 1, -1, -1):
        next_pos = robot[i] + 1
        if next_pos == n - 1:
            robot.pop(i)
        else:
            robot[i] = next_pos
    return [a[-1]] + a[0:-1]    

def move():
    global cnt
    for i in range(len(robot) - 1, -1, -1):
        next_pos = robot[i] + 1
        if a[next_pos] > 0 and next_pos not in robot:
            a[next_pos] -= 1
            if a[next_pos] == 0:
                cnt += 1
            if next_pos == n - 1:
                robot.pop(i)
            else:
                robot[i] = next_pos
            
def charge():
    global cnt
    if a[0] > 0:
        a[0] -= 1
        robot.insert(0, 0)
        if a[0] == 0:
            cnt += 1


n, k, a = init()
robot = []

t = 1
cnt = 0
while True:
    a = belt_rotate(a)
    move()
    charge()
    if cnt >= k:
        break
    t += 1
print(t)