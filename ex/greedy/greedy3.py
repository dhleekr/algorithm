data = input()

res = 0

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        res += 1

if res%2 == 0:
    print(res//2)
else:
    print(res//2 + 1)