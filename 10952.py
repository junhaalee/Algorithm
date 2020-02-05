temp = []

while(sum != 0):
    a, b = map(int, input().split())
    sum = a+b
    if sum != 0:
        temp.append(sum)

for i in range(len(temp)):
    print(temp[i])