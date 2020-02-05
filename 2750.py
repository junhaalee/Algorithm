n = int(input())
temp = []
for i in range(n):
    temp.append(int(input()))
temp.sort()
for i in range(n):
    print(temp[i])