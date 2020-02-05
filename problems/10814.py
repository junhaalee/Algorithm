n = int(input())

temp = []

for _ in range(n):
    age, name = input().split()
    temp.append([int(age),name])


ans = sorted(temp, key = lambda x : x[0])

for i in range(n):
    print(ans[i][0], ans[i][1])