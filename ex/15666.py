def init():
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = set(numbers)
    numbers = list(numbers)
    numbers.sort()
    return N, M, numbers

def backtracking(idx, selected):
    if selected == M:
        print(' '.join(map(str, num_list)))
        return

    if idx == len(numbers):
        return

    num_list[selected] = numbers[idx]
    backtracking(idx, selected+1)
    num_list[selected] = 0
    backtracking(idx+1, selected)

N, M, numbers = init()
num_list = [0]*M
backtracking(0, 0)