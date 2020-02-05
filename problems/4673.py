
def d(n):
    num = str(n)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum+n

result = []

for i in range(1, 100):
    if d(i) < 100:
        result.append(d(i))
result.sort()

for i in range(1,100):
    if i not in result:print(i)

