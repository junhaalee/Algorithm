n = int(input())
temp = []
for i in range(n):
    temp.append(input())

temp = list(set(temp))

temp.sort(key = lambda x : (len(x),x))

for i in temp:
    print(i)