from itertools import combinations

temp = []

for _ in range(9):
    temp.append(int(input()))

ans = list(combinations(temp,7))

for i in range(len(ans)):
    if sum(ans[i]) == 100:
        result = list(ans[i])
        break
result.sort()
for i in range(7):
    print(result[i])
