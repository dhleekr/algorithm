n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1] # 동 남 서 북
dj = [1, 0, -1, 0]

dice = [1, 2, 3, 4, 5, 6]
