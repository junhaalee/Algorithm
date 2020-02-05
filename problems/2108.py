from collections import Counter
n = int(input())

temp = []

for i in range(n):
    temp.append(int(input()))
temp.sort()
num_count=dict(Counter(temp))

result = sorted(num_count.items(), key = (lambda x : x[1]), reverse=True)

print(round(sum(temp)/n))

if len(result) == 1:
    print(result[0][0])
else:
    print(temp[int(len(temp)/2)-1])

if len(result) == 1:
    print(result[0][0])
elif result[0][1] == result [1][1]:
    print(result[1][0])
else:
    print(result[0][0])

print(max(temp)-min(temp))
