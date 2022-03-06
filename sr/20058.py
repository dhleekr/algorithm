def init():
    n, q = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(2**n)]
    L = list(map(int, input().split()))