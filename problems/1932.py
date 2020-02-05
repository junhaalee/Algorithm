n = int(input())
temp = []
for _ in range(n):
    temp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(temp[i])):
        if j == 0:
            temp[i][j] = temp[i][j] + temp[i-1][0]
        elif j == len(temp[i])-1:
            temp[i][j] = temp[i][j] + temp[i-1][-1]
        else:
            temp[i][j] = temp[i][j] + max(temp[i-1][j-1], temp[i-1][j])

print(max(temp[n-1])) 
