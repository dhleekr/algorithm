def custom_sort(array):
    temp = dict()
    for i in array:
        if i not in temp.keys() and i > 0:
            temp[i] = 1
        elif i > 0:
            temp[i] += 1
    temp_array = []
    for k, v in temp.items():
        temp_array.append([k, v])
    temp_array.sort(key=lambda x: (x[1], x[0]))

    sorted_array = []
    for a in temp_array:
        sorted_array.extend(a)

    return sorted_array

def R(arr):
    for i in range(len(arr)):
        new = custom_sort(arr[i])
        arr[i] = new
    max_len = max(len(row) for row in arr)

    for i in arr:
        if len(i) < max_len:
            i.extend([0] *(max_len - len(i)))
    return arr

def transpose(arr):
    row = len(arr)
    col = len(arr[0])
    new_arr = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            new_arr[j][i] = arr[i][j]
    return new_arr


r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for _ in range(3)]

t = 0
while t < 101:
    if 0 <= r < len(arr) and 0 <= c < len(arr[0]) and arr[r][c] == k:
        break

    if len(arr) >= len(arr[0]):
        arr = R(arr)
    else:
        arr = transpose(arr)
        arr = R(arr)
        arr = transpose(arr)
    t += 1

if t == 101:
    print(-1)
else:
    print(t)