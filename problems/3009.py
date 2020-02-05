X = []
Y = []

for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = []

for i in range(3):
    if X.count(X[i]) == 1: ans.append(X[i])
for i in range(3):
    if Y.count(Y[i]) == 1: ans.append(Y[i])

print(ans[0],ans[1])