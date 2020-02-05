n,m,k = map(int, input().split())

team = 0
while(True):
    if n <= 1 or m == 0:
        break
    else:
        n -= 2
        m -= 1
        team += 1

k = k-(n+m)
while(True):
    if k <= 0:
        break
    else:
        k -= 3
        team -= 1

print(team)