n, k = map(int, input().split())

bag = [list(map(int, input().split())) for _ in range(n)]

bag = sorted(bag, key = lambda x : x[1])

sol = [0 for _ in range(k+1)]

for i in range(n):
    for j in range(k,1,-1):
        if bag[i][0] <= j:
            sol[j] = max(sol[j], sol[j-bag[i][0]]+bag[i][1])

print(max(sol))
