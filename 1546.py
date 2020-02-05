size = int(input())
scores = list(map(int, input().split()))

temp = []
for i in range(size):
    temp.append((scores[i]/max(scores))*100)

print(sum(temp)/size)
