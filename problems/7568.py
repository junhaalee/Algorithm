n = int(input())

temp = []

for _ in range(n):
    h,w = map(int, input().split())
    temp.append([h,w])

for i in range(n):
    count = 1
    for j in range(n):
        if temp[i][0] < temp[j][0] and temp[i][1] < temp[j][1] : count += 1
    print(count,end = ' ')


