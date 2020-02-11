case = [int(input()) for _ in range(int(input()))]

ans = [1,1,1]

for i in range(3, max(case)):
    ans.insert(i, ans[i-2]+ans[i-3])

for i in range(len(case)):
    print(ans[case[i]-1])