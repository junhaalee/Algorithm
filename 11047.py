n, price = map(int, input().split())

coin = []

for _ in range(n):
    coin.append(int(input()))

coin = coin[::-1]

count = 0

ind = 0

while(True):

    if price == 0:
        break

    if coin[ind] <= price:
        count = count + int(price/coin[ind])
        price = price%coin[ind]

    else:
        ind += 1

print(count)