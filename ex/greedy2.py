num = input()

res = 0

for s in num:
    if (n:= int(s)) <= 1 or res == 0:
        res += n
    else:
        res *= n
print(res)