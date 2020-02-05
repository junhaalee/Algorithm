n = int(input())

rope = []

for _ in range(n):
    rope.append(int(input()))

rope.sort()
ans = 0
for i in range(n):
    if ans < rope[i]*(n-i): ans = rope[i]*(n-i)

print(ans)