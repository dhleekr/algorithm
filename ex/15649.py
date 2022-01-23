def backtracking():
    if len(array) == M:
        print(' '.join(map(str, array)))
        return

    for i in range(1, N+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()


N, M = map(int, input().split())
array = []
backtracking()