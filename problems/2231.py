n = int(input())
temp = []

for i in range(n):
    val = i+sum(map(int, list(str(i))))
    if val == n:
        temp.append(i)
if len(temp) >= 1:
    print(min(temp))
else:
    print(0)
