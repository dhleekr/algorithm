def make_order(x, y):
    order = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cd = 0
    step = 0
    while True:
        if cd % 2 == 0:
            step += 1
        flag = True
        for _ in range(step):
            y += dy[cd]
            x += dx[cd]
            order.append((x,y))
            if x == 0 and y == 0:
                flag = False
                break
        if not flag:
            break
        cd = (cd+1) % 4

    return order

def grid_to_list(grid, order):
    store = []
    for x, y in order:
        store.append(grid[y][x])
    
    return store

def list_to_grid(store, order):
    grid = []
    for _ in range(N):
        grid.append([0]*N)

    for i in range(len(store)):
        x = order[i][0]
        y = order[i][1]
        grid[y][x] = store[i]

    return grid

def pull_marbles(store):
    for i in reversed(range(len(store))):
        if store[i] == 0:
            store.pop(i)    
    return store

def boom(store):
    boom_list = []
    while True:
        continuity = [] # 연속되는 구슬들의 index 넣어주는 리스트
        temp = [] # 일시적으로 index 넣어주고 나중에 continuity 리스트에 추가할 거
        cnt = 1
        for i in range(len(store)-1):
            if store[i] == store[i+1]:
                cnt += 1
                if i not in temp:
                    temp.append(i)
                temp.append(i+1)

                if i == len(store)-2 and cnt >= 4:
                    cnt = 1
                    continuity.extend(temp)
                    temp = []
            else:
                if cnt >= 4: # 터뜨리는 부분
                    cnt = 1
                    continuity.extend(temp)
                    temp = []
                else:
                    cnt = 1
                    temp = []
        
        if not continuity:
            break

        for idx in reversed(continuity):
            boom_list.append(store.pop(idx))
    
    return store, sum(boom_list)

def marble_change(store, N):
    new_store = []
    length = N**2 - 1
    stop = False
    while store:
        cnt = 0
        try:
            while store[0] == store[0+cnt]:
                cnt += 1
        except:
            pass
        
        for i in range(cnt):
            if i == 0:
                if len(new_store) <= length-2:
                    new_store.append(cnt)
                    new_store.append(store.pop(0))
                else:
                    stop = True
                    break
            else:
                store.pop(0)
            
        if stop:
            break

    return new_store

# 입력 받기
N, M = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]

x = N//2
y = N//2

# 방향 설정 (위, 아래, 왼, 오)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
order = make_order(x, y)

ans = 0

for _ in range(M):
    d, s = list(map(int, input().split()))
    # 구슬 파괴
    for i in range(s+1):
        grid[y + i*dy[d-1]][x + i*dx[d-1]] = 0
    
    # 순서대로 리스트로 만들기
    store = grid_to_list(grid, order)
    
    # 구슬 당기기
    store = pull_marbles(store)

    # 연속 구슬 폭발
    store, boom_sum = boom(store)
    ans += boom_sum

    # 구슬 변화 -> 전체 칸보다 구슬 수가 많아지면 뒤에 구슬들은 그냥 사라짐
    store = marble_change(store, N)
    grid = list_to_grid(store, order)


print(ans)