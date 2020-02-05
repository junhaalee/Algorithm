T = input()

split_p = T.split('-')

for i in range(len(split_p)):
    if '+' in split_p[i]:
        split_p[i] = sum(list(map(int, split_p[i].split('+'))))

ans = int(split_p[0])

for i in range(0,len(split_p)-1):
    ans -= int(split_p[i+1])
print(ans)