temp = input().split('-')
ans = sum(list(map(int, temp[0].split('+'))))
for i in range(1, len(temp)):
    ans -= sum(list(map(int, temp[i].split('+'))))
print(ans)