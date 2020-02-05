n = int(input())

wine = [int(input()) for _ in range(n)]

result = [0, wine[0]]

if n > 1 :
    result.append(wine[0]+wine[1])

for i in range(3, n+1):
    result.append(
        max(
            wine[i-1] + wine[i-2] + result[i-3],
            wine[i-1] + result[i-2],
            result[i-1]
        )
    )

print(result[n])