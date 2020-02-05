n = int(input())
temp = []
for i in range(n):
    temp.append(list(map(int, input().split())))

temp.sort(key = lambda x : (x[0],x[1]))

for i in range(n):
    print(temp[i][0], temp[i][1])