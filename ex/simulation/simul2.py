numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

data = input()

alphabet = []
num = []
for c in data:
    if c in numbers:
        num.append(int(c))
    else:
        alphabet.append(c)

num_sum = sum(num)
alphabet.sort()

res = ''
for alpha in alphabet:
    res += alpha

res += str(num_sum)

print(res)