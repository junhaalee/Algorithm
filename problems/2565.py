n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
line = sorted(line, key = lambda x : x[0])

result = [1]*n

for i in range(1, n):
    count = 0
    for j in range(i):
        if line[i][1] > line[j][1]:
            count = max(count, result[j])
    result[i] = count + 1

print(n-max(result))
