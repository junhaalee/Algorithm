time = sorted([list(map(int, input().split())) for _ in range(int(input()))],key = lambda x : (x[1],x[0]))

result = [time[0]]

for i in range(1, len(time)):
    if time[i][0] >= result[-1][1]:
        result.append(time[i])

print(len(result))