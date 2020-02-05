n = int(input())

for i in range(n):
    num, ch = input().split()

    ans = ''

    for j in range(len(ch)):
        for k in range(int(num)):
            ans += ch[j]
    
    print(ans)