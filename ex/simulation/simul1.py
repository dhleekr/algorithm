num = input()

mid = len(num)//2

first, last = num[:mid], num[mid:]

first_sum = 0
last_sum = 0

for f, l in zip(first, last):
    first_sum += int(f)
    last_sum += int(l)

if first_sum == last_sum:
    print("LUCKY")
else:
    print("READY")