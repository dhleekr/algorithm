def init():
    N, K = list(map(int, input().split()))

    belt = list(map(int, input().split()))

    return N, K, belt

def move(a):
    new = []
    new.append(a.pop())
    new.extend(a)

    return new

N, K, belt = init()
robots = [0]*2*N
ans = 1

while True:
    belt = move(belt)
    robots = move(robots)
    robots[N-1] = 0

    for i in reversed(range(N-1)):
        if robots[i] == 1 and robots[i+1] == 0 and belt[i+1] >= 1:
            belt[i+1] -= 1
            robots[i] = 0
            robots[i+1] = 1
    robots[N-1] = 0
    
    if robots[0] == 0 and belt[0] >= 1:
        robots[0] = 1
        belt[0] -= 1

    if belt.count(0) >= K:
        break

    ans += 1
    
print(ans)