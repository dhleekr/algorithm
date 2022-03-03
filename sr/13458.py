def init():
    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())
    return n, a, b, c

n, a, b, c = init()

cnt = 0
for num in a:
    num -= b
    cnt += 1
    if num > 0:
        if num % c == 0:
            cnt += num // c
        else:
            cnt += num // c + 1   

print(cnt)