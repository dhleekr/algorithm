T = int(input())

answer = []

for test_case in range(T):
    a, value = input().split()
    a = int(a)
    value = int(value, 16)
    value = bin(value)[2:]
    if len(value) < a*4:
        value = '0'*(a*4-len(value))+value

    answer.append(value)


for i in range(len(answer)):
    print(f'#{i+1}', answer[i])