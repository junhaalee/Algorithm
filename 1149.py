T = int(input())

price = []

for _ in range(T):
    price.append(list(map(int, input().split())))

ans = []
ind = []


for i in range(len(price)):
    ans.append(min(price[i]))
    ind.append(price[i].index(min(price[i])))

for i in range(2, len(price)):
    if ind[i] == ind[i-1] and ind[i] == ind[i-2]:
        temp = ans[i-2:i+1]
        price[i+temp.index(max(temp))-2][ind[i+temp.index(max(temp))-2]] += max(price[i+temp.index(max(temp))-2])
        ans[i+temp.index(max(temp))-2] = min(price[i+temp.index(max(temp))-2])
        ind[i+temp.index(max(temp))-2] = price[i+temp.index(max(temp))-2].index(min(price[i+temp.index(max(temp))-2]))

print(sum(ans))


