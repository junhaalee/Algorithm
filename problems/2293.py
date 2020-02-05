n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

n = 3
k = 10
coin =[1,2,5]

result = [1]+[0]*k

for i in coin:
    for j in range(i, k+1):
        result[j] += result[j-i]




