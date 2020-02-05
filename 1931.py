T = int(input())

case = []

for i in range(T):
    case.append(list(map(int, input().split())))

case = sorted(case, key = lambda x : (x[1],x[0]) )

ans = [case[0]]

for i in range(1,len(case)):

    if case[i][0] >= ans[-1][1]: ans.append(case[i])

print(len(ans))