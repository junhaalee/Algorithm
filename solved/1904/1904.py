n = int(input())

ans = [1,2]

for i in range(2, n):
    ans.insert(i,ans[i-1]%15746+ans[i-2]%15746)

print(ans[-1]%15746)