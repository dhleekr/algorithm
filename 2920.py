a = list(map(int, input().split()))

ascending = True
descending = True

for i in range(len(a)-1):
    if a[i] <= a[i+1]:
        descending = False
    else:
        ascending = False

if ascending:
    print('ascending')

if descending:
    print('descending')

if ascending != True and descending != True:
    print('mixed')