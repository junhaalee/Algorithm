a, b = input().split()
dif = len(b) - len(a)
ans = []

for i in range(dif+1):
    temp = 0
    for j in range(i, len(a)+i):
        if a[j-i] != b[j] : temp += 1
    ans.append(temp)
print(min(ans))