n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

total = 0
for num in a:
    remain = num - b
    total += 1
    if remain > 0:
        if remain % c == 0:
            total += remain // c
        else:
            total += remain // c + 1
     
print(total)