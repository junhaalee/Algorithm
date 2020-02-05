price = 1000-int(input())

re = [500,100,50,10,5,1]

count = 0

i = 0

while(True):

    if price == 0 : break

    if re[i] <= price:
        count += int(price/re[i])
        price %= re[i]

    else: i += 1

print(count)