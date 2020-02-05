n = int(input())
temp = []
for _ in range(n):
    temp.append(int(input()))

temp.sort()

for i in range(n):
    print(temp[i])