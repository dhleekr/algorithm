def init():
    N = int(input())
    blocks = []
    for _ in range(N):
        block = list(map(int, input().split()))
        blocks.append(block)

    return N, blocks

def block_move(block):
    t, x, y = block

    # green
    g_idx = 0
    if t == 1 or t == 3:
        for i in range(6):
            if green[i][y] == 1:
                break
            g_idx += 1
        green[g_idx-1][y] = 1
        if t == 3:
            green[g_idx-2][y] = 1
    else:
        for i in range(6):
            if green[i][y] == 1 or green[i][y+1] == 1:
                break
            g_idx += 1
        green[g_idx-1][y] = 1
        green[g_idx-1][y+1] = 1


    # blue
    b_idx = 0
    if t == 1 or t == 2:
        for j in range(6):
            if blue[j][3-x] == 1:
                break
            b_idx += 1
        blue[b_idx-1][3-x] = 1
        if t == 2:
            blue[b_idx-2][3-x] = 1
    else:
        for j in range(6):
            if blue[j][3-x] == 1 or blue[j][2-x] == 1:
                break
            b_idx += 1
        blue[b_idx-1][3-x] = 1
        blue[b_idx-1][2-x] = 1
            
def block_boom(): 
    green_score = 0
    blue_score = 0
    # green
    for i in range(6):
        if green[i] == [1, 1, 1, 1]:
            green_score += 1

            for idx in reversed(range(i)):
                green[idx+1] = green[idx]
                green[idx] = [0, 0, 0, 0]

    for j in range(6):
        if blue[j] == [1, 1, 1, 1]:
            blue_score += 1

            for idx in reversed(range(j)):
                blue[idx+1] = blue[idx]
                blue[idx] = [0, 0, 0, 0]

    return green_score, blue_score

def light_color_check():
    for i in range(2):
        if sum(green[i]) != 0:
            green[1:] = green[:5]
            green[0] = [0, 0, 0, 0]
        
        if sum(blue[i]) != 0:
            blue[1:] = blue[:5]
            blue[0] = [0, 0, 0, 0]


N , blocks = init()

green, blue = [[0]*4 for _ in range(6)], [[0]*4 for _ in range(6)]
ans = 0
for idx, block in enumerate(blocks):
    block_move(block)
    green_score, blue_score = block_boom()
    ans += green_score + blue_score

    light_color_check()

block_sum = 0
for i in range(6):
    block_sum += sum(green[i])
    block_sum += sum(blue[i])

print(ans)
print(block_sum)