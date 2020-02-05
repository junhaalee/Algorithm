temp = []
for i in range(10):
    temp.append(int(input())%42)
print(len(set(temp)))