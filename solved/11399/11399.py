n = int(input())
time = sorted(list(map(int, input().split())))

ans = 0
for i in range(len(time)):
    ans += (time[i]*(len(time)-i))

print(ans)