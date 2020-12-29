n, m = map(int, input().split())
if n >= m:
    print(n-m)
else:
    dp = [0]*100001
    temp = [m]
    count = 1
    while(True):
        if dp[n] != 0:
            break
        arr = []
        for t in temp:
            if t<100000 and dp[t+1] == 0:
                dp[t+1] = count
                arr.append(t+1)

            if dp[t-1] == 0 :
                dp[t-1] = count
                arr.append(t-1)

            if t%2 == 0 and dp[t//2] == 0:
                dp[t//2] = count
                arr.append(t//2)
        temp = arr
        count += 1
    print(dp[n])