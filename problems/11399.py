T = int(input())
num = list(map(int, input().split()))
num.sort()
for i in range(1,T):
    num[i] += num[i-1]
print(sum(num))